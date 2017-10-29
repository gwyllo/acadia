from __future__ import absolute_import, division, print_function

import os.path
import re
import sys
import glob
import json
import shutil
from collections import defaultdict
import numpy as np
from six.moves import urllib
from annoy import AnnoyIndex
from scipy import spatial
from nltk import ngrams
import random, json, glob, os, codecs, random
import numpy as np
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('image_file', '', """Absolute path to image file.""")
tf.app.flags.DEFINE_string(
    'model_dir', '/tmp/imagenet',
    """Path to classify_image_graph_def.pb, """
    """imagenet_synset_to_human_label_map.txt, and """
    """imagenet_2012_challenge_label_map_proto.pbtxt.""")

#config
infiles = glob.glob('image_vectors/*.npz')
dims = 2048
t = AnnoyIndex(dims)

def create_graph():
  """Creates a graph from saved GraphDef file and returns a saver."""
  # Creates graph from saved graph_def.pb.
  with tf.gfile.FastGFile(os.path.join(
      FLAGS.model_dir, 'classify_image_graph_def.pb'), 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')


#get activations for image
def get_feature_vector(imagePath):
	#create graph and get tensorflow session
	create_graph()
	
	with tf.Session() as sess:
		#try open the file
		try:
			print("parsing", imagePath, "\n")
			if not tf.gfile.Exists(imagePath):
			  tf.logging.fatal('File does not exist %s', imagePath)
			  
			with tf.gfile.FastGFile(imagePath, 'rb') as f:
			  image_data =  f.read()
			  feature_tensor = sess.graph.get_tensor_by_name('pool_3:0')
			  feature_set = sess.run(feature_tensor,{'DecodeJpeg/contents:0': image_data})
			  feature_vector = np.squeeze(feature_set)
			  return feature_vector
		except:
			print('could not process image', imagePath)
#get n nearest neighbours
def get_neighbours(featureVector):
	#load tree and get neighbours
	t.load('tree.ann') 
	nearest_neighbours = t.get_nns_by_vector(featureVector, 3, search_k=-1, include_distances=False)
	return nearest_neighbours
	
#search for similar images
def search(image):
	feature_vector = get_feature_vector(image)
	return get_neighbours(feature_vector)

def main(_):
	image = glob.glob(sys.argv[1])[0]
	image_name = image.split('.')[0]
	image_indexes = search(image)
	#create json for output
	if not os.path.exists('search_results/'+image_name):
		os.makedirs('search_results/'+image_name)
	file_list = os.listdir('image_vectors')
	#get image name of closest file
	closest_file = file_list[image_indexes[0]][:-4]
	shutil.copyfile('data/drawings/'+closest_file, 'search_results/'+image_name+'/'+closest_file)
	
	named_nearest_neighbors = []
	for file_index in image_indexes:
		neighbour_file_name = file_list[file_index]
		named_nearest_neighbors.append({ 'filename': neighbour_file_name})
		
	with open('search_results/' + image_name +'/'+image_name + '.json', 'w') as out:
		json.dump(named_nearest_neighbors, out)
	print("all done")
	#return location of closest file for twitter bot
	return 'data/drawings/'+closest_file
	
	
if __name__ == '__main__':
	tf.app.run()
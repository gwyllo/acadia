import Image
import os
import os.path
import sys

#folder_path = sys.argv[0]
#alternatively put the script in the folder you want to work with and set variable here
folder_path = "./"

def sortImages(imageDir):
	images = [f for f in os.listdir(imageDir) if os.path.isfile(os.path.join(imageDir, f))]
	
	small_dir = os.path.join(imageDir,"small")
	if(not os.path.exists(small_dir)):
		os.makedirs(small_dir)
	big_dir = os.path.join(imageDir,"big")
	if(not os.path.exists(big_dir)):
		os.makedirs(big_dir)

	for image in images:
		old_path = os.path.join(imageDir,image)
	
		img = Image.open(old_path)
	
		if(img.size[0]<200):
			new_path = os.path.join(small_dir,image)
			os.rename(old_path,new_path)
		else:
			print "big" + image
			new_path = os.path.join(big_dir,image)
			os.rename(old_path,new_path)

for root, dirs, files in os.walk(folder_path, topdown=False):
    for name in dirs:
	if(name=="full"):
		imagedir = os.path.join(root, name)
		sortImages(imagedir)




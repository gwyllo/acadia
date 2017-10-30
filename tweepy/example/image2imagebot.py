# image2imagebot.py

# the name of the acc

#subprocess to run shell script
import subprocess
# os for path management
import os

import random
from io import BytesIO
from twittersecrets import *
import requests
import tweepy
from PIL import Image
from PIL import ImageFile
import random
import sys

tracking_tag=handle
ml_script=sys.argv[1]

ImageFile.LOAD_TRUNCATED_IMAGES = True

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Twitter requires all requests to use OAuth for authentication
auth.set_access_token(access_token, access_secret) 
api = tweepy.API(auth)

# Called when a new status arrives which is passed down from the on_data method of the StreamListener
def tweet_image(url, username, status_id):
    print("... Loading image")
    filename = 'temp.png'
    # send a get request
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        # read data from downloaded bytes and returns a PIL.Image.Image object
        i = Image.open(BytesIO(request.content))
        # Saves the image under the given filename
        i.save(filename)
        new_filename = process_image(filename)
        # scramble(filename)
        # Update the authenticated users status
        api.update_with_media(new_filename, status='@{0}'.format(username), in_reply_to_status_id=status_id)
    else:
        print("Error: Unable to download image")

def execute_shell(cmd):
    print("... Executing command: "+cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for c in iter(p.stdout.readline, ''):
        print(c)
    p.wait()
        
def process_image(filename):
    print("... Processing image")
    randImageId = str(int(random.random()*1000000000))

    tarPath="./twitter/twitter_"+randImageId+".png"

    execute_shell(ml_script+" "+filename+" "+tarPath)
    
    return tarPath


# create a class inheriting from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):   
    def on_status(self, status):
        #dont respond to replies, only new tweets
            username = status.user.screen_name
            status_id = status.id 
            
            print (">>>> TWEET RECEIVED ------------------------------------")
            print (status.text)
            
            if 'media' in status.entities:
                for image in status.entities['media']:
                    tweet_image(image['media_url'], username, status_id)
            else:
                 print ("Error: Tweet did not contain any media")
            print ("END ------------------------------------")


print ("INITIALISING     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
myStreamListener = BotStreamer()
print("... Listening for..."+tracking_tag)
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=[tracking_tag])
print ("SESSION ENDED    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

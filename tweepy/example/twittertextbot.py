# twittertextbot.py

import tweepy

# import our keys
from twittersecrets import *

# connect to twitter using our keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

api.update_status(status="Hello World!")

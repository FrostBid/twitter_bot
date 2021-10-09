"""Main module."""
import tweepy
import logging
import os
from secret import *

auth = tweepy.OAuthHandler(apikey, apisecret)
api = tweepy.API(auth)
auth.set_access_token(accesstoken, accesstokensecret)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



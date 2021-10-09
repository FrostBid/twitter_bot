"""Main module."""
import tweepy
import logging
import os
from secret import *
import json
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(apikey, apisecret)
api = tweepy.API(auth)
auth.set_access_token(accesstoken, accesstokensecret)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


days = 2994
while True:
    api.update_status(f"It has been {days} days since the release of GTA 5, still no release of GTA 6...\n#GTA6 #GTA #GTA5")
    days += 1
    sleep(86400)
    print('Tweet successful')



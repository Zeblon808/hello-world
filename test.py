import tweepy as tw
import pandas as pd
from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
import numpy as np 
import json



consumer_key= 'Zt3OYo2IyFuhox5c4pRHeVgJE'
consumer_secret= 'fNEJXJ2GKJvwWO5iGv7EaKMj3jjblCYy79Xy8UveBtqZEb81AR'
access_token= '1115425620-KFVBWIasxHNrEnviYyfpqtYafCkNwkLwtPU1XWu'
access_token_secret= 'PHlVz5nrfyjgZBP5gkR8PS2lJ0qg0JQ2Uuetrgk3R59aO'



auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

username = "@letourdata"
date_since = "2019-06-01"


# Collect tweets
tweets = tw.Cursor(api.user_timeline,
              screen_name=username,
              lang="en",
              since=date_since).items(6)

# Iterate on tweets
for tweet in tweets:
    print(tweet.text)


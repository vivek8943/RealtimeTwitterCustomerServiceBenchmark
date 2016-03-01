'''
Created on Sep 24, 2015

@author: Vivek
'''

import time
import tweepy
from datetime import datetime
import pika
import json
from pymongo import MongoClient
from textblob import TextBlob

def producer():
    CONSUMER_KEY = 'AefnuQaRarn28kcbg2xiihW3B'
    CONSUMER_SECRET = '5dBq93YIWrqdGVT0ckXh5Wh5Yc1JkDdSOskQaWpCVTyKykEjln'
            # The access tokens can be found on your applications's Details
            # page located at https://dev.twitter.com/apps (located
            # under "Your access token")
    ACCESS_TOKEN = '154053454-xvTmai7aAmyBpTkXjCWhmqaVNsshiDfQjhu8drrm'
    ACCESS_TOKEN_SECRET = 'GVKSsQY62S21cFlwr97Z0TVb47JIThDF7CZ9kGQz6Y6Zq'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # cheat: year, month, day, hour, minute, second, microsecond
   
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
            # set max queue size
    args = {"x-max-length": 2000}
    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    channel.queue_declare(queue='twitter_topic_feed')
    
    for tweet in tweepy.Cursor(api.search, q="@Delta", since="2015-01-09", result_type='recent', lang="en").items():
        data = {}
        posts = db.posts10
        data['created_at'] = tweet.created_at
        data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
        data['text'] = tweet.text
        data['id_str'] = tweet.id_str
        data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
        data['geo'] = tweet.geo
        data['friends_count'] = tweet.user.friends_count
        data['in_reply_to_screen_name'] = tweet.in_reply_to_screen_name
        data['in_reply_to_user_id'] = tweet.in_reply_to_user_id
        data = json.dumps(str(data))
        """tweet = TextBlob(tweet.text)
            score=tweet.sentiment.polarity
            print(tweet.sentiment.polarity)
            avg={}
            scores_plot={}
            now = time.strftime("%c")
            scores_plot[now]=score
            avg[now]=scores_plot[now]/len(scores_plot)
            score_json=json.dumps(avg)
            print (avg)
            """
        channel.basic_publish(exchange='', routing_key='twitter_topic_feed', body=data)
            
            # tweet=json.dumps(tweet)
            # print(tweet)
                 # tweetit=json.loads(tweet)
                 # simplejson.loads('created_at',str(tweet))
                 # print(tweet[u'text'])
            # list(posts.find())[:2]
           # print(created_at.__len__())
    
    # def removeCollection():
    
producer()    
    
    
    
    

'''
Created on Sep 21, 2015
This script uses tweepy to get data from twitter using certain criteria and then store it in mongodb

@author: Vivek
'''



import tweepy
from datetime import datetime
from pymongo import MongoClient
import json
def main():
        # The consumer keys can be found on your application's Details
        # page located at https://dev.twitter.com/apps (under "OAuth settings")
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
    return api


def connectionFactory():
    client = MongoClient('localhost', 27017)
    db = client.twitterdatadelta
    return db

def getTweets(api, db):
    for tweet in tweepy.Cursor(api.search, q="@Delta", since="2015-01-09", result_type='recent', lang="en").items():
        posts = db.posts12
        data = {}
        data['created_at'] = tweet.created_at
        data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
        data['text'] = tweet.text
        data['id_str'] = tweet.id_str
        data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
        data['geo'] = tweet.geo
        data['friends_count'] = tweet.user.friends_count
        data['in_reply_to_screen_name'] = tweet.in_reply_to_screen_name
        data['in_reply_to_user_id'] = tweet.in_reply_to_user_id
        # print(tweet.created_at)
        print(data)
        posts.insert(data)
        print(posts.find().count())
        
        # cursor = posts.find({'created_at':{"$gt":date1}})
        # print(cursor.next())
        # print(tweet.text,tweet.in_reply_to_status_id,tweet.id,tweet.created_at,tweet.id_str,tweet.source,tweet.in_reply_to_screen_name,tweet.created_at)

api = main()
db = connectionFactory()
getTweets(api, db)

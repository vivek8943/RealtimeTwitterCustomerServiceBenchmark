"""
GetReplies.py connects to twitter using Tweepy which uses the twitter api and get all the replies
 from the required userhandle specified in screenname parameter of the search API.Once tweets are received we store them in the dataBase
"""
from pymongo import MongoClient
import tweepy
import json
def main():
  # Variables that contains the user credentials to access Twitter API
      CONSUMER_KEY = 'AefnuQaRarn28kcbg2xiihW3B'
      CONSUMER_SECRET = '5dBq93YIWrqdGVT0ckXh5Wh5Yc1JkDdSOskQaWpCVTyKykEjln'
          # The access tokens can be found on your applications's Details
          # page located at https://dev.twitter.com/apps (located
          # under "Your access token")
      ACCESS_TOKEN = '154053454-xvTmai7aAmyBpTkXjCWhmqaVNsshiDfQjhu8drrm'
      ACCESS_TOKEN_SECRET = 'GVKSsQY62S21cFlwr97Z0TVb47JIThDF7CZ9kGQz6Y6Zq'
      auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
      auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      api = tweepy.API(auth)
      return api
def connectionFactory():

    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    return db

def getTweets(api, db):
    '''
    
    :param api:
    :param db:
    '''
    for tweet in tweepy.Cursor(api.user_timeline, screen_name='@Delta', since='2015-09-01', result_type='recent').items():

     if tweet.in_reply_to_status_id_str != None:
         posts = db.posts11
         data = {}
         data['geo'] = tweet.geo

         data['created_at'] = tweet.user.created_at
         data['in_reply_to_status_id_str'] = tweet.in_reply_to_status_id_str
         data['screen_name'] = tweet.user.screen_name
         data['text'] = tweet.text
         data['id_str'] = tweet.id_str
         data['friends_count'] = tweet.user.friends_count
         data['in_reply_to_screen_name'] = tweet.in_reply_to_screen_name
         data['in_reply_to_user_id'] = tweet.in_reply_to_user_id
         data['screen_name'] = tweet.user.screen_name

         print(data)
         posts.insert(data)
         print(posts.find().count())

api = main()
db = connectionFactory()
getTweets(api, db)

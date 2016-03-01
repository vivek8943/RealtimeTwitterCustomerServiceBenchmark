from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json



# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")

consumer_key = 'AefnuQaRarn28kcbg2xiihW3B'
consumer_secret = '5dBq93YIWrqdGVT0ckXh5Wh5Yc1JkDdSOskQaWpCVTyKykEjln'

access_token_key = '154053454-xvTmai7aAmyBpTkXjCWhmqaVNsshiDfQjhu8drrm'
access_token_secret = 'GVKSsQY62S21cFlwr97Z0TVb47JIThDF7CZ9kGQz6Y6Zq'




class StdOutListener(StreamListener):
    def on_data(self, data):

       
        tweet = json.loads(data)
        print(tweet)
        
    
        # is this a geocoded tweet?
        geo = tweet['geo']
        if geo and geo['type'] == 'Point':
            # collect location of mrt station
            coords = geo['coordinates']
            print('viv')
            print coords
        return True

    def on_error(self, status):
        print('status: %s' % status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    stream = Stream(auth, l, timeout=60)

    print("Listening to filter stream...")

    stream.filter(track=['@DeltaAssist'], locations=[-70.93044414, 41.65536809, -70.9231071, 41.66316909])

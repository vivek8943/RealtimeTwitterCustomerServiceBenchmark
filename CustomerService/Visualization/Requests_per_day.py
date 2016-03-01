'''
Created on Sep 22, 2015

@author: Vivek
This script gets the 
'''

from datetime import timedelta, date
from pymongo import MongoClient
import json
def main():
   
    start_date = date(2013, 1, 1)
    end_date = date(2015, 6, 2)
    for single_date in daterange(start_date, end_date):
        print single_date.strftime("%Y-%m-%d")  # var: year, month, day, hour, minute, second, microsecond
        pass
 
def connectionFactory(flag):

    
    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    
    return db

def getCustomerServiceTweets(posts1, posts2, date1, date2):
    customer_service_count = posts1.find({"created_at": {"$gte": date1, "$lt": date2}}).count()
    delta_tweets_count = posts2.find({"created_at": {"$gte": date1, "$lt": date2}}).count()
    json_counts = [{"Handle": "DeltaAssist", "tweets": customer_service_count}, {"Handle": "Delta", "tweets":delta_tweets_count}]
    json_counts = json.dumps(json_counts)
    return json_counts

def getCounts():
   
    date1, date2 = main()
    db = connectionFactory(1)
    posts1 = db.posts10
    client = MongoClient('localhost', 27017)
    db = client.twitterdatadelta
    posts2 = db.posts12
    json_count = getCustomerServiceTweets(posts1, posts2, date1, date2)
    return json_count

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


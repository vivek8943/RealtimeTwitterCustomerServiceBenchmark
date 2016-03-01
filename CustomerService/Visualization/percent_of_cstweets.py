'''
This script gets the distribution of tweets to various service handles
Created on Sep 21, 2015

@author: Vivek
'''
import datetime

from pymongo import MongoClient
from datetime import datetime as dt
import json
json_counts = []
def main():
   
    # var: year, month, day, hour, minute, second, microsecond
    date1 = dt.strptime("1/09/15 ", "%d/%m/%y ")
    date2 = dt.strptime("1/11/15 ", "%d/%m/%y ")
    dayDelta = datetime.timedelta(days=1)
    return date1, date2, dayDelta

 
def connectionFactory(flag):

    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    return db

def getCustomerServiceTweets(posts1, posts2, date1, date2, dayDelta):
    global json_counts
    dataR = []
    dayDelta = datetime.timedelta(days=1)
    temp = 0
    temp2 = 0
    
    while date1 < date2:
        month_val = date1.strftime("%B")
        
        if(date1.strftime("%B") == month_val):
            date1 += dayDelta
            customer_service_count = posts1.find({"created_at": {"$gte": date1, "$lt": date1 + dayDelta }}).count()
            # print customer_service_count,'is the count on',date1
            temp = customer_service_count + temp
            delta_tweets_count = posts2.find({"created_at": {"$gte": date1, "$lt": date1 + dayDelta }}).count()
            temp2 = delta_tweets_count + temp2
            # print month_val,temp,temp2
            if(date1.strftime("%B") != month_val) :
                dataR.append({"Handle": month_val, "Cstweets": temp, "dtweets":temp2}) 
                temp = 0
                temp2 = 0
                print dataR
                
    json_counts = json.dumps(dataR)
        # print json_counts
    return json_counts

def getCounts():
   
    date1, date2, dayDelta = main()
    db = connectionFactory(1)
    posts1 = db.posts10
    
    client = MongoClient('localhost', 27017)
    db = client.twitterdatadelta
    
    posts2 = db.posts12
    json_count = getCustomerServiceTweets(posts1, posts2, date1, date2, dayDelta)
    return json_count

# print counts

'''
Created on Oct 4, 2015

@author: Vivek
'''

from pymongo import MongoClient
from textblob import TextBlob
import json
from datetime import datetime as dt
import datetime

class getimpression:
    
    def get_pos_imp(self):
        
        print "in get_pos_imp"
        client = MongoClient('localhost', 27017)
        db = client.twitterdata
        timeseriesinfo = []
        
        posts = db.posts10
        created_at = []
        bad_potential_imp = []
        good_potential_imp = []
        startDate = dt.strptime("1/09/15 ", "%d/%m/%y ")
        endDate = dt.strptime("30/10/15 ", "%d/%m/%y ")
        dayDelta = datetime.timedelta(days=1)
        
       
        while startDate < endDate:
           
           
            startDate += dayDelta
        
        
        
            count = posts.find({"created_at":{"$gte": startDate, "$lt": startDate + dayDelta }}).count()
            for d in posts.find({"created_at": {"$gte": startDate, "$lt": startDate + dayDelta}}):
                    # print(d['created_at'])
                    posts = db.averagetweesentimentimpression
                    tweet = TextBlob(d["text"])
                    # print(tweet.sentiment.polarity)
                    
                    created_at.append(tweet.sentiment.polarity)
                    
                  #  print(tweet)
                    if(tweet.sentiment.polarity < 0.5):
                               bad_potential_imp.append(d['friends_count'])
                               timeseriesinfo.append({
                               'date': d['created_at'],
                               'count': tweet.sentiment.polarity,
                               'potential_reach':d['friends_count']
                                    })
                       
                   
        
                    else:   
                        good_potential_imp.append(d['friends_count'])    
                           
                    
                    json_counts = [{"Date":startDate.day , "Reach": good_potential_imp.count(), "TotalRequests":count}]
        json_counts = json.dumps(json_counts)
        print 'impr', json_counts
        return json_counts
    
        
       
        
        
        
        

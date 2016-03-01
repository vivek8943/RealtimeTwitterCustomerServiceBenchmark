"""
This script queries the mongodb to get the tweets over a range of dates and also has functions to calculate
 the positive reach of the tweets and negative reach of tweets.
 We used textblob to get tweet polarity 
"""
import json
import datetime
from pymongo import MongoClient
from datetime import datetime as dt
from textblob import TextBlob

class getcsreq:
    trend = 0
    def __init__(self, trend):
        self.trend = trend

   
    def getCsreq(self):
        dataR = []
       
        client = MongoClient('localhost', 27017)
        db = client.twitterdata
        posts = db.posts10
        startDate = dt.strptime("1/09/15 ", "%d/%m/%y ")
        endDate = dt.strptime("30/10/15 ", "%d/%m/%y ")
        dayDelta = datetime.timedelta(days=self.trend)
        
        while startDate < endDate:
           
           
           startDate += dayDelta
          
           count = posts.find({"created_at":{"$gte": startDate, "$lt": startDate + dayDelta }}).count()
           # counts_req["day"][startDate.day]=count
           # json_counts.appends({"Day": startDate.day,"No of requests": count})
           if(self.trend == 7):
               if(startDate.day == 8):
                     dataR.append({
                    'date':"Week 1",
                    'count': count
                    })
               elif(startDate.day == 15):   
                     dataR.append({
                    'date':"Week 2",
                    'count': count
                    }) 
               elif(startDate.day == 22):
                      dataR.append({
                    'date':"Week 3",
                    'count': count
                    })     
               elif(startDate.day == 29):
                     dataR.append({
                    'date':"Week 4",
                    'count': count
                    })         
                      
           else:
                dataR.append({
                'date': startDate.strftime("%x"),
                'count': count
                })
           # counts_req[startDate.day]=count
               

        
        data = json.dumps(dataR)
        
        return data 
       
    def get_pos_imp(self):
        dataR = []
        print "in impression"      
        client = MongoClient('localhost', 27017)
        db = client.twitterdata
        posts = db.posts10
        startDate = dt.strptime("1/09/15 ", "%d/%m/%y ")
        endDate = dt.strptime("30/09/15 ", "%d/%m/%y ")
        dayDelta = datetime.timedelta(days=1)
        
        while startDate < endDate:
           
            startDate += dayDelta
        
            potential_imp = 0
            for d in posts.find({"created_at": {"$gte": startDate, "$lt": startDate + dayDelta}}):
                    # print(d['created_at'])
                    # posts = db.averagetweesentimentimpression
                    tweet = TextBlob(d["text"])
                    # print(tweet.sentiment.polarity)
                    
                  #  print(tweet)
                    if(tweet.sentiment.polarity > 0):
                              potential_imp = potential_imp + (d['friends_count'])
                              """timeseriesinfo.append({
                               'date': d['created_at'],
                               'count': tweet.sentiment.polarity,
                               'potential_reach':d['friends_count']
                                    })"""
            dataR.append({"Date":startDate.strftime("%x") , "Reach":potential_imp
                })        
                  
        
                    
                    
        print  dataR   
        json_counts = json.dumps(dataR)
                    # print 'impr',json_counts
        return json_counts    
    
    def get_neg_imp(self):
        dataR = []
             
      
        client = MongoClient('localhost', 27017)
        db = client.twitterdata
        
        posts = db.posts10
        
        
        
        startDate = dt.strptime("1/09/15 ", "%d/%m/%y ")
        endDate = dt.strptime("30/09/15 ", "%d/%m/%y ")
        dayDelta = datetime.timedelta(days=1)
        
       
        while startDate < endDate:
           
           
            startDate += dayDelta
        
        
        
            potential_neg_imp = 0
            for d in posts.find({"created_at": {"$gte": startDate, "$lt": startDate + dayDelta}}):
                    # print(d['created_at'])
                    # posts = db.averagetweesentimentimpression
                    tweet = TextBlob(d["text"])
                    # print(tweet.sentiment.polarity)
                    
                   
                    

                  #  print(tweet)
                    if((tweet.sentiment.polarity) < (-0.5)):
                              potential_imp = potential_neg_imp + (d['friends_count'])
                              """timeseriesinfo.append({
                               'date': d['created_at'],
                               'count': tweet.sentiment.polarity,
                               'potential_reach':d['friends_count']
                                    })"""
            dataR.append({"Date":startDate.strftime("%x") , "Reach":potential_imp
                })        
            print dataR       
        
                    
                    
           
        json_counts = json.dumps(dataR)
                    # print 'impr',json_counts
        return json_counts    
        
     
        

     

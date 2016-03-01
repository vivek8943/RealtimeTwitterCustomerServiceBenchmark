"""
AverageScorePerDay.py ....This script gets the tweets from the MongoDb using the MongoClient from the Pymongo package by querying the database 
based upon certain criterion(Range of Dates)

Once we get the tweet we extract the text from the tweet and use the TextBlob package to get the sentiment score of the tweet and then compute 
the average per day
Once the average is computed we send the result as a Json response over HTTP to the client which has sent the request to plot the graph for 
visualization 

"""
import json
import datetime
from pymongo import MongoClient
from textblob import TextBlob
from datetime import datetime as dt
created_at = []
def getAvgScorePerDay():
    '''
    
    '''
    dataR = []
    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    posts = db.posts10
   
    startDate = dt.strptime("1/09/15 ", "%d/%m/%y ")
    endDate = dt.strptime("30/09/15 ", "%d/%m/%y ")
    dayDelta = datetime.timedelta(days=1)
    
    while startDate < endDate:
       
       
       startDate += dayDelta
      
       for d in posts.find({"created_at":{"$gte": startDate, "$lt": startDate + dayDelta }}):
       # counts_req["day"][startDate.day]=count
       # json_counts.appends({"Day": startDate.day,"No of requests": count})
     
            tweet = TextBlob(d["text"])
            # print(tweet.sentiment.polarity)
            created_at.append(tweet.sentiment.polarity)
          #  print(tweet)
    
            score = sum(created_at) / (created_at.__len__())
            
            # tweet=json.dumps(tweet)
            dataR.append({
            'date': startDate.day,
            'count': score
            })
       # counts_req[startDate.day]=count
       
    
    data = json.dumps(dataR)
    print data
    return data 
getAvgScorePerDay()      

          

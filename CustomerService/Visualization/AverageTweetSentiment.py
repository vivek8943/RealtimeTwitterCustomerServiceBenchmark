"""

AverageScorePerDay.py ....This script gets the tweets from the MongoDb using the MongoClient from the Pymongo package by querying the database 
based upon certain criterion(Range of Dates)

Once we get the tweet we extract the text from the tweet and use the TextBlob package to get the sentiment score of the tweet and then compute 
the average for given date range

Once the average is computed we send the result as a Json response over HTTP to the client which has sent the request to plot the graph for 
visualization 

"""



from pymongo import MongoClient
from textblob import TextBlob
import json
from datetime import datetime as dt
import datetime

def get_art():
    # cheat: year, month, day, hour, minute, second, microsecond
    date1 = dt.strptime("25/09/15 ", "%d/%m/%y ")
    date2 = dt.strptime("5/10/15 ", "%d/%m/%y ")
    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    posts = db.posts10
    created_at = []
    dataR = []
    
                   
    dayDelta = datetime.timedelta(days=1)
    while date1 < date2:
            month_val = date1.strftime("%B")
            if(date1.strftime("%B") == month_val):
                date1 += dayDelta
                for d in posts.find({"created_at": {"$gte": date1, "$lt": date2}}):
                # print(d['created_at'])
                    tweet = TextBlob(d["text"])
                    created_at.append(tweet.sentiment.polarity)
                    score = (sum(created_at)) / (created_at.__len__())
                if(date1.strftime("%B") != month_val) :
                    dataR.append({"Month": month_val, "Score": score}) 
                    # print dataR    
    # json_counts=[{"Metric": "Average Tweet Sentiment","Score": score}]
    json_counts = json.dumps(dataR)
           # posts.insert(bad_potential_imp)
    return json_counts
   
    
    
    
  

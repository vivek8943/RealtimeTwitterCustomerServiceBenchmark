from pymongo import MongoClient
from textblob import TextBlob
from datetime import datetime


# cheat: year, month, day, hour, minute, second, microsecond
date1 = datetime.strptime("1/09/15 ", "%d/%m/%y ")
date2 = datetime.strptime("18/09/15 ", "%d/%m/%y ")

print(date1)
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.twitterdata
collection = db.tweetCollection
posts = db.posts10
created_at = []


for d in posts.find({"created_at": {"$gte": date1, "$lt": date2}}):
        print(d['created_at'])
        tweet = TextBlob(d["text"])
        print(tweet.sentiment.polarity)
        created_at.append(tweet.sentiment.polarity)
      #  print(tweet)

        print(sum(created_at) / (created_at.__len__()))
        # tweet=json.dumps(tweet)
        # print(tweet)
             # tweetit=json.loads(tweet)
             # simplejson.loads('created_at',str(tweet))
             # print(tweet[u'text'])
        # list(posts.find())[:2]
       # print(created_at.__len__())

# def removeCollection():







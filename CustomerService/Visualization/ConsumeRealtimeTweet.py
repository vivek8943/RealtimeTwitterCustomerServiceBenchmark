'''
Created on Sep 24, 2015

@author: vivek
'''
from pymongo import MongoClient
import pika
def consumers():
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_consume(callback, queue='twitter_topic_feed', no_ack=True)    
    print ' [*] Waiting for messages. To exit press CTRL+C'
    channel.start_consuming()
    
        # print(sum(created_at)/(created_at.__len__()))
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    #posts.insert(body)
    return body

client = MongoClient('localhost', 27017)
db = client.twitterdata
posts = db.posts10
consumers()

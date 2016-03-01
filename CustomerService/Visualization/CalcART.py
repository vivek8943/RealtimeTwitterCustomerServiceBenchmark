"""
This script gets the requests for Customer service and the replies for the requests and finds out the response time using the unique 
id of the tweet and the reply_to tweet id from mongodb

"""
from pymongo import MongoClient
from datetime import datetime
def get_response_time():
    # cheat: year, month, day, hour, minute, second, microsecond
    date1 = datetime.strptime("1/09/06 00:00", "%d/%m/%y %H:%M")
    date2 = datetime.strptime("31/10/15 00:05", "%d/%m/%y %H:%M")
    
    
    client = MongoClient('localhost', 27017)
    db = client.twitterdata
    
    posts = db.posts10
    complaint_id = {}
    posts1 = db.posts11
    reply_id = {}
    
    for d in posts.find({"created_at": {"$gte": date1, "$lt": date2}}):
        one = d['id_str']  # tweet id from a cs request to deltaAssist
        complaint_id[one] = d['created_at']
        # print('afterfirstfor')
    
    for d in posts1.find():
        # print('in 2 for')
        two = d['in_reply_to_status_id_str']
        reply_id[two] = d['created_at']
        
    f = open('art.txt', 'w')
    for key_comp_id in complaint_id:
        
        for key_rep_id in reply_id:
            if(key_comp_id == key_rep_id):
                print("got one match")
                print(str(reply_id[key_rep_id] - complaint_id[key_comp_id]))
                f.write(str(reply_id[key_rep_id] - complaint_id[key_comp_id]))
                # print(complaint_id)
get_response_time()                

"""
After receiving the request from the client Url.py figures out which action is to be performed based on the URL and this views.py file

has  all the respective actions or the links to business logic and returns a response to the client.

"""
from django.shortcuts import  render_to_response
from django.template.context import RequestContext
from AverageTweetSentiment import get_art
from django.http import HttpResponse
import percent_of_cstweets
import json
from Visualization import  CsRequestPerDay
# from Visualization.ProduceRealtimeTweet import producer
# from Visualization import ConsumeRealtimeTwitterSentiment

"""from ProduceRealtimeTweetSentiment import producer
from ConsumeRealtimeTwitterSentiment import consumers"""
def login(request):
   
    return render_to_response(('index.html'), context_instance=RequestContext(request))
def percentageofcs(request):
    
    counts = percent_of_cstweets.getCounts()
    return HttpResponse(counts, content_type='application/json')
   
"""def realTimeTweetSentiment():
    producer()
    json_tweet_score=ConsumeRealtimeTwitterSentiment
    return HttpResponse(json_tweet_score, content_type='application/json')"""
def dashboard(request):
   # data={"foo": "bar"}
    
    return render_to_response('Dashboard.html', context_instance=RequestContext(request))
def impressionpage(request):
   # data={"foo": "bar"}
    
    return render_to_response('Impression.html', context_instance=RequestContext(request))

def csreqperday(request): 
           '''
            
            :param request:
            '''
           obj = CsRequestPerDay.getcsreq(1) 
           data = obj.getCsreq() 
           return HttpResponse(data, content_type='application/json')
def csreqperweek(request):
           obj = CsRequestPerDay.getcsreq(7) 
           data = obj.getCsreq() 
           return HttpResponse(data, content_type='application/json')
def impression(request):
           obj = CsRequestPerDay.getcsreq(7) 
           data = obj.get_pos_imp() 
           return HttpResponse(data, content_type='application/json')
def negimpression(request):
           obj = CsRequestPerDay.getcsreq(7) 
           data = obj.get_neg_imp() 
           return HttpResponse(data, content_type='application/json')       
def Avescore(request):
           data = get_art() 
           return HttpResponse(data, content_type='application/json')
def responsetime(request):
           print "inresponsetime" 
           dataR = []
           dataR = ({"Handle":'September', "Cstweets":'45', "dtweets":'53'}, {"Handle":'October', "Cstweets":'28', "dtweets":'39'}) 
           data = json.dumps(dataR)
           return HttpResponse(data, content_type='application/json')       
def Avescoreperday():
    data = get_art() 
    return HttpResponse(data, content_type='application/json')

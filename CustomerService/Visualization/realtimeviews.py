from django.shortcuts import  render_to_response
from django.template.context import RequestContext



def score(request):
   # data={"foo": "bar"}
    
    return render_to_response('Realtime.html', context_instance=RequestContext(request))

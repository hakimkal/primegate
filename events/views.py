from django.shortcuts import *
from django.template  import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from events.models import Event
from news.models import News
from nlsubscribers.forms import NlsubscriberForm
import datetime



def index(request):
    
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    news = News.objects.order_by('-created')[:5]
    #events = Event.objects.order_by('-start_date')[:5]
    cssClass = "page-sub-page page-events-listing page-microsite"
    event_list = Event.objects.order_by("-created").all()
    paginator = Paginator(event_list,5)
    
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'current_date':now
              ,
              'theyear': theyear,
              'news': news,
              
              'cssClass':cssClass,
              'nlform': nlsubscriber_form
              }
    
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    myDict['events']= events    
    return render(request, "events/index.html", myDict)

def detail(request,id):
    
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    news = News.objects.order_by('-created')[:5]
    #events = Event.objects.order_by('-start_date')[:5]
    cssClass = "page-sub-page page-events-listing page-microsite"
    event= Event.objects.get(pk=id)
    
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'current_date':now
              ,
              'theyear': theyear,
              'news': news,
              
              'cssClass':cssClass,
              'nlform': nlsubscriber_form
              }
    
    
    myDict['event']= event    
    return render(request, "events/event_detail.html", myDict)
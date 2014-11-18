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
    events = Event.objects.order_by('-start_date')[:3]
    cssClass = "page-sub-page page-microsite"
    event_list = Event.objects.all()
    paginator = Paginator(event_list,5)
    
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'current_date':now
              ,
              'theyear': theyear,
              'news': news,
              'events': events,
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
    return render(request, "events/index.html", myDict)
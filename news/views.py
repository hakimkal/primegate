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
    thenews = News.objects.order_by('-created')[:4]
    #events = Event.objects.order_by('-start_date')[:3]
    cssClass = 'page-sub-page page-blog-listing page-microsite'
    
    news_list = News.objects.order_by("-created").all()
    paginator = Paginator(news_list,6)
    
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'current_date':now
              ,
              'theyear': theyear,
              'thenews': thenews,
              
              'cssClass':cssClass,
              'nlform': nlsubscriber_form
              }
    
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    myDict['news']= news
    return render(request, "news/index.html", myDict)

def detail(request, news_id):
    
    cssClass = "page-sub-page page-blog-detail page-microsite"    
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    news = News.objects.order_by("-created").all()[:4]
    
    thenews = News.objects.get(pk=news_id)
    #print thenews.user.first_name
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'current_date':now
              ,
              'theyear': theyear,
              
              'news': news,
              'cssClass':cssClass,
              'nlform': nlsubscriber_form
              }
    
    
    myDict['thenews']= thenews    
    return render(request, "news/news_detail.html", myDict)
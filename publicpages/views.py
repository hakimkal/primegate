from django.shortcuts import *
from django.template  import RequestContext
from publicpages.forms import *
from events.models import Event
from news.models import News
from team.models import Team
from testimonials.models import Testimonial
from nlsubscribers.forms import NlsubscriberForm
from homepagebanners.models import Homepagebanner
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    news = News.objects.order_by('-created')[:3]
    events = Event.objects.order_by('-start_date')[:3]
    banners = Homepagebanner.objects.order_by('-created').all()[:5]
    cssClass = "page-sub-page page-microsite"
    testimonials = Testimonial.objects.order_by('-created')[:5]
    nlsubscriber_form = NlsubscriberForm()
    return render(request,'publicpages/index.html',{'banners':banners,'testimonials':testimonials,'events':events,'news':news,'current_date':now,'theyear': theyear,'cssClass': cssClass,'nlform':nlsubscriber_form})

def about(request):
    now = datetime.datetime.now()
    cssClass= " page-sub-page page-about-us page-microsite"
    theyear= datetime.datetime.today().year
    return render(request, 'publicpages/about.html',{'current_date':now, 'theyear': theyear,'cssClass': cssClass})

def contact(request):
    nlsubscriber_form = NlsubscriberForm()
    news = News.objects.order_by('-created')[:5]
    now = datetime.datetime.now()
    cssClass = "page-sub-page page-contact page-microsite"
    theyear= datetime.datetime.today().year
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name  = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data["message"]
            cc_myself = 'info@leproghrammeen.com'
            
            recipients = ['abdulhakim.haliru@leproghrammeen.com']
        if cc_myself:
            recipients.append(email)
            send_mail("Primegate Website Visitor", message, email, recipients)
            txt = 'Thanks for writing us, we will be in touch'    
            return render_to_response('publicpages/contact.html',{'form':form, 'current_date':now, 'theyear': theyear,'success' :  txt,'cssClass': cssClass}, context_instance = RequestContext(request))
    else:
        
        return render_to_response('publicpages/contact.html',{'nlform':nlsubscriber_form,'news':news,'current_date':now,
                                                              'theyear': theyear,'form':FeedbackForm(),'cssClass': cssClass},context_instance = RequestContext(request))


def team(request):
    nlsubscriber_form = NlsubscriberForm()
    team_list = Team.objects.all()
    paginator = Paginator(team_list,5)
    news = News.objects.order_by('-created')[:5]
     
    cssClass ="page-sub-page page-members page-microsite"
    now = datetime.datetime.now()
    theyear= datetime.datetime.today().year
    page = request.GET.get('page')
    try:
        team = paginator.page(page)
    except PageNotAnInteger:
        team = paginator.page(1)
    except EmptyPage:
        team = paginator.page(paginator.num_pages)
    return render(request, 'publicpages/team.html',{'team':team,'nlform':nlsubscriber_form,'news':news,'current_date':now, 'theyear': theyear,'cssClass':cssClass})
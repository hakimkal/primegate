from django.shortcuts import render
from faqs.models import Faq
from news.models import News
from nlsubscribers.forms import NlsubscriberForm
import datetime
def index(request):
    faqs = Faq.objects.all()
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    cssClass = "page-sub-page page-members page-microsite"
    news  =  News.objects.order_by('-created')[:5]
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'faqs':faqs,'nlform':nlsubscriber_form,'news':news,'current_date':now, 'theyear': theyear,'cssClass':cssClass}
    return render(request,'publicpages/faqs.html',myDict,)
 
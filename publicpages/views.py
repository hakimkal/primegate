from django.shortcuts import *
from django.template  import RequestContext
from publicpages.forms import *
from django.core.mail import send_mail
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    cssClass = "page-sub-page page-microsite"
    return render(request,'publicpages/index.html',{'current_date':now,'theyear': theyear,'cssClass': cssClass})

def about(request):
    now = datetime.datetime.now()
    cssClass= " page-sub-page page-about-us page-microsite"
    theyear= datetime.datetime.today().year
    return render(request, 'publicpages/about.html',{'current_date':now, 'theyear': theyear,'cssClass': cssClass})

def contact(request):
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
        
        return render_to_response('publicpages/contact.html',{'current_date':now,
                                                              'theyear': theyear,'form':FeedbackForm(),'cssClass': cssClass},context_instance = RequestContext(request))


def team(request):
    cssClass ="page-sub-page page-members page-microsite"
    now = datetime.datetime.now()
    theyear= datetime.datetime.today().year
    return render(request, 'publicpages/team.html',{'current_date':now, 'theyear': theyear,'cssClass':cssClass})
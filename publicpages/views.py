from django.shortcuts import render
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
    return render(request, 'publicpages/contact.html',{'current_date':now, 'theyear': theyear,'cssClass': cssClass})


def team(request):
    cssClass ="page-sub-page page-members page-microsite"
    now = datetime.datetime.now()
    theyear= datetime.datetime.today().year
    return render(request, 'publicpages/team.html',{'current_date':now, 'theyear': theyear,'cssClass':cssClass})
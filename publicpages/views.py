from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    return render(request,'publicpages/index.html',{'current_date':now,'theyear': theyear})
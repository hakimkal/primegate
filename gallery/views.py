from django.shortcuts import render
from django.template  import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from nlsubscribers.forms import NlsubscriberForm
from gallery.models import Gallery
import datetime
def index(request):
    
    now = datetime.datetime.now()
    theyear = datetime.datetime.today().year
    cssClass = "page-sub-page page-members page-microsite"
    gallery_list = Gallery.objects.order_by("-created").all()
    nlsubscriber_form = NlsubscriberForm()
    myDict = {'nlform':nlsubscriber_form,'current_date':now, 'theyear': theyear,'cssClass':cssClass}
    paginator = Paginator(gallery_list,15)
    
    page = request.GET.get('page')
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        gallery = paginator.page(1)
    except EmptyPage:
        gallery = paginator.page(paginator.num_pages)
    myDict['galleries']= gallery
    return render(request,'gallery/gallery.html',myDict,)
 
    
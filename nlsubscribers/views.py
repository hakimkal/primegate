from django.contrib import messages
from django.shortcuts import render,redirect

from nlsubscribers.models import Nlsubscriber


from nlsubscribers.forms import NlsubscriberForm


def nladd(request):
    if request.method == 'POST':
        form = NlsubscriberForm(request.POST)
        if form.is_valid():
            
            nlsub = form.save()
            messages.success(request, "Thank you for subscribing for our newsletters.")
            return redirect('/')
        else:
            messages.error(request, "Oops something went wrong, We could not take that information!")
            return redirect("/")
    else:
        messages.error(request, "Invalid request method")
        return redirect('/about/')
        
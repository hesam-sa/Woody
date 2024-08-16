from django.shortcuts import render
from .forms import NewsLetterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request,'website/index.html')

def contact_view(request):
    return render(request,'website/contact.html')

def about_view(request):
    return render(request,'website/about.html')

def feature_view(request):
    return render(request,'website/feature.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your Comment Submitted Successfully Wait for admin to improve')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Your Comment Not Submitted') 
            return HttpResponseRedirect('/')
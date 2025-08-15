from django.shortcuts import render,redirect
from .forms import NewsLetterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index_view(request):
    return render(request,'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your Message Submitted Successfully")
        else:
            messages.add_message(request,messages.ERROR,"Your Message Not Submitted")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def about_view(request):
    return render(request,'website/about.html')

def feature_view(request):
    return render(request,'website/feature.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your Email Submitted Successfully')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Your Email Not Submitted') 
            return HttpResponseRedirect('/')
        
def custom_404_view(request, exception):
   context = {}
   return render(request,'admin/404.html', context)

def error_500(request):
   context = {}
   return render(request,'admin/500.html', context)
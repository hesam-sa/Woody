from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
        try:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'You are Logged In')
                return redirect('/')
        except UnboundLocalError:
                messages.add_message(request,messages.ERROR,'Your username or password is Incorrect ')
                return redirect('/')
    form = AuthenticationForm()    
    context = {'form': form}    
            
    return render(request,'accounts/login.html',context)
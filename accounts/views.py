from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from blog.models import UserProfile
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password =form.cleaned_data.get('password')
            try:
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,'You are Logged In Successfully')
                    return redirect('/')
            except UnboundLocalError:
                    messages.add_message(request,messages.ERROR,'Your username or password is Incorrect ')
                    return redirect('/accounts/login')
    else:
        messages.add_message(request,messages.ERROR,f'You are already logged in as {request.user.username}')
        return redirect('/')
    form = AuthenticationForm()    
    context = {'form': form}    
            
    return render(request,'accounts/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
              
                form.save()
                
                messages.add_message(request,messages.SUCCESS,'New User Is Created')
                return redirect('/accounts/login')
            else:
                messages.add_message(request,messages.ERROR,'New User Is Not Created')
    else:
        messages.add_message(request,messages.ERROR,f'You are already logged in as {request.user.username} You should Log Out First' )
        return redirect('/')
    form=UserCreationForm()
    context={'form':form}
    return render(request,'accounts/signup.html',context)
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CustomUserCreationForm,UserForm
from django.contrib import messages
from django.contrib.auth.models import User

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
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
              
                form.save()
                
                messages.add_message(request,messages.SUCCESS,'New User Is Created')
                return redirect('/accounts/login')
            else:
                messages.add_message(request,messages.ERROR,'New User Is Not Created')
    else:
        messages.add_message(request,messages.ERROR,f'You are already logged in as {request.user.username} You should Log Out First' )
        return redirect('/')
    form=CustomUserCreationForm()
    context={'form':form}
    return render(request,'accounts/signup.html',context)

def profile_view(request):
    username = request.user.username
    
    if request.method == 'POST':
            
            user = User.objects.get(username=username)
            form = UserForm(request.POST)

            if form.is_valid():
                user.first_name=form.cleaned_data.get('first_name')
                user.last_name=form.cleaned_data.get('last_name')
                user.email=form.cleaned_data.get('email')
                user.save()
                
                
                messages.add_message(request,messages.SUCCESS,'profile Complete')
                return redirect('/accounts/login')
            else:
                messages.add_message(request,messages.ERROR,'Not submitted')
    
    form = UserForm()
    context={'form':form}
    return render(request,'accounts/profile.html',context)

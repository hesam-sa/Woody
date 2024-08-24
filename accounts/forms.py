from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import UserProfile

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name","last_name","email")

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)

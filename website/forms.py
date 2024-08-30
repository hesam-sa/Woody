from django import forms
from .models import NewsLetter,Contact
from captcha.fields import CaptchaField

class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = "__all__"

class ContactForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'
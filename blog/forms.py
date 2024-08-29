from django import forms
from .models import Comment,Post
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message','user']

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Post
        fields = ['title','content','author','category','image','tags','status','login_required','captcha']
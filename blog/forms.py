from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message','user']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','author','category','image','tags','status']
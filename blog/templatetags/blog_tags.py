from django import template
from blog.models import UserProfile,Post,Comment
from django.contrib.auth.models import User
from website.models import Contact


register = template.Library()

@register.inclusion_tag('website/team.html')
def profiles():
    
    posts = UserProfile.objects.exclude(user="3")
    return {'posts':posts}

@register.inclusion_tag('website/popularpost.html')
def popularposts():
    
    posts = Post.objects.all().order_by('-counted_view')[:6]
    return {'posts':posts}

@register.inclusion_tag('website/details.html')
def details():

    posts = Post.objects.all()
    comments = Comment.objects.all()
    comments_count = comments.count()
    posts_count = posts.count()
    user_count = User.objects.all().count()
    view = 0
    for i in posts:
        view += i.counted_view

    return {'view':view,'comments_count':comments_count,'posts_count':posts_count,'user_count':user_count}

@register.inclusion_tag('website/testimonial.html')
def messages():
    
    contacts = Contact.objects.all().order_by('-created_date')[:3]
    
    return {'contact1':contacts[0],'contact2':contacts[1],'contact3':contacts[2]}

    
from django import template
from blog.models import UserProfile,Post


register = template.Library()

@register.inclusion_tag('website/team.html')
def profiles():
    
    posts = UserProfile.objects.exclude(user="3")
    return {'posts':posts}

@register.inclusion_tag('website/popularpost.html')
def popularposts():
    
    posts = Post.objects.all().order_by('-counted_view')[:6]
    return {'posts':posts}
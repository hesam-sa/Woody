from django import template
from blog.models import UserProfile

register = template.Library()

@register.inclusion_tag('website/team.html')
def profiles():
    
    posts = UserProfile.objects.exclude(user="3")
    return {'posts':posts}
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('<int:pid>',single_view,name='single'),
    
]
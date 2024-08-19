from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('<int:pid>',single_view,name='single'),
    path('comment',comment_view,name='comment'),
    path("author/<str:author_name>",blog_view,name='author')
    
]
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('<int:pid>',single_view,name='single'),
    path('comment',comment_view,name='comment'),
    path("author/<str:author_name>",blog_view,name='author'),
    path('newpost',newpost_view,name='newpost'),
    path("remove/<int:remove_id>",blog_view,name='remove'),
    path("tags/<str:tag_name>",blog_view,name='tags'),
    path("category/<str:cat_name>",blog_view,name='cat'),
]
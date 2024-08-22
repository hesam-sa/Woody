from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login',login_view,name='login'),
    # path('<int:pid>',single_view,name='single'),
    # path('comment',comment_view,name='comment'),
    # path("author/<str:author_name>",blog_view,name='author'),
    # path('newpost',newpost_view,name='newpost'),
    # path("remove/<int:remove_id>",blog_view,name='remove'),
]
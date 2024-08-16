from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('',index_view,name='home'),
    path('contact',contact_view,name='contact'),
    path('about',about_view,name='about'),
    path('features',feature_view,name='features'),
    path('newsletter',newsletter_view,name='newsletter')

]
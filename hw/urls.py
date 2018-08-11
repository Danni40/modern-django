#from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.homePageView, name='home')
]

#from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

urlpatterns = [
    url('', views.homePageView, name='home')
]
'''
router = routers.DefaultRouter()
router.register(r'', views.homePageView, name='home')

urlpatterns = [
    url(r'', include(router.urls)),
]
'''
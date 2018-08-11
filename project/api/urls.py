from django.conf.urls import url, include
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

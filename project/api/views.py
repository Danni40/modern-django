from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer
from django.http import HttpResponse

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

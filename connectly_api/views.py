from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

# Create your views here.

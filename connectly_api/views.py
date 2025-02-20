from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def authenticate():
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]

class UserViewSet(viewsets.ModelViewSet):
    authenticate()
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    authenticate()
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    authenticate()
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer

# Create your views here.

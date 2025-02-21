from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Post, Comment, Like
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer
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

class LikeViewSet(viewsets.ModelViewSet):
    authenticate()

    # list all likes of a post
    def list(self, request):
        post = request.query_params.get('post')
        queryset = Like.objects.filter(post=post).order_by('created_at')
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # like or unlike a post
    def create(self, request):
        serializer = LikeSerializer(data=request.data)
        # check if user has already liked the post
        user = request.data['user']
        post = request.data['post']
        like = Like.objects.filter(user=user, post=post)
        if like:
            # delete the like
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # create the like
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    
# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Post, Comment, Like, Feed
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer, FeedSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly

def authenticate():
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]

class UserViewSet(viewsets.ModelViewSet):
    authenticate()
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    authenticate()

    serializer_class = PostSerializer
    # queryset = Post.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        user_id = self.request.user.id
        if user.is_authenticated:
            return Post.objects.filter(Q(author=user_id) | Q(private=False))
            # return Post.objects.filter(private=False) | Post.objects.filter(author=user_id)
        return Post.objects.filter(private=False)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # def list(self, request):
    #     return Post.objects.all()
        # serializer = PostSerializer(queryset, many=True)
        # return Response(serializer.data)

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

class FeedCustomPagination(PageNumberPagination):
    authenticate()
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

  
class FeedViewSet(viewsets.ModelViewSet):
    authenticate()
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    pagination_class = FeedCustomPagination  # Use custom pagination
    
# Create your views here.

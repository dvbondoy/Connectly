from django.contrib import admin
from .models import User, Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')
    
# Register your models here.


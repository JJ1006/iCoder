from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # API to post comments
    path('postComment', views.postComment, name='postComment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]

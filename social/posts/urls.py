from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Create,Update,Delete,LikePost,CommentPost
from user.VerifyToken import VerifyToken
from django.urls import re_path


urlpatterns = [
    path('create/', csrf_exempt(VerifyToken(Create.as_view()))),
    re_path(r'^update/(?P<pk>[0-9a-f-]+)/$', csrf_exempt(VerifyToken(Update.as_view())), name='update_post'),
    re_path(r'^delete/(?P<pk>[0-9a-f-]+)/$', csrf_exempt(VerifyToken(Delete.as_view())), name='delete_post'),
    
    #like post
    re_path(r'^like/(?P<pk>[0-9a-f-]+)/$',csrf_exempt(VerifyToken(LikePost.as_view())),name="like_post"),
    re_path(r'^like/(?P<pk>[0-9a-f-]+)/$',csrf_exempt(VerifyToken(LikePost.as_view())),name="like_post"),
    
    
    #comment
    re_path(r'^comment/(?P<pk>[0-9a-f-]+)/$',csrf_exempt(VerifyToken(CommentPost.as_view())),name="comment_post"),
    
 ]
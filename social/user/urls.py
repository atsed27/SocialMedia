from django.urls import path,re_path
from .views import RegisterView,LoginView,GetUser,Follower
from .VerifyToken import VerifyToken
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('signin/',LoginView.as_view()),
    
    #Test Token 
    path ('auth/user/',VerifyToken(GetUser.as_view())),
    
    
     #follow
    re_path(r'^follow/(?P<pk>[0-9a-f-]+)/$',csrf_exempt(VerifyToken(Follower.as_view())),name="follow"),
    
]
from django.urls import path
from .views import RegisterView,LoginView,GetUser
from .VerifyToken import VerifyToken

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('signin/',LoginView.as_view()),
    
    #Test Token 
    path ('auth/user/',VerifyToken(GetUser.as_view())),
    
]
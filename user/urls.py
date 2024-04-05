from django.urls import path
from .views import RegisterView,LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('auth/signin/',LoginView.as_view()),
]
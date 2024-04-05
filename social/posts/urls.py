from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import Create
from user.VerifyToken import VerifyToken

urlpatterns = [
    path('create/', csrf_exempt(VerifyToken(Create.as_view()))),
   
]
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Create,Update
from user.VerifyToken import VerifyToken
from django.urls import re_path


urlpatterns = [
    path('create/', csrf_exempt(VerifyToken(Create.as_view()))),
    re_path(r'^update/(?P<pk>[0-9a-f-]+)/$', csrf_exempt(VerifyToken(Update.as_view())), name='update_post'),

 ]
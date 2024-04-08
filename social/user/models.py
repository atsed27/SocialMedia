from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#follower and following model
class UserFollow(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="src_follow")
    following = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="dest_following")
    follows = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="dest_follow")
    
from rest_framework import serializers
from .models import User,UserFollow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserFollow
        fields="__all__"

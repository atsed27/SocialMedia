from rest_framework import serializers
from .models import Post,PostLike,PostComment


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    


class PostCommentSerialize(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'
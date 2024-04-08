from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers,PostLikeSerializer,PostCommentSerialize
from user.models import User
from .models import Post,PostLike,PostComment
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


import uuid

# Create your views here.

class Create(APIView):
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        findUser = User.objects.filter(id=request.userId).first()

        #save
        serializer.save(user=findUser)
        
        return Response(serializer.data)


class Update(APIView):
    def put(self, request, pk):
        # Find Post
        findPost = Post.objects.filter(id=pk).first()
        if findPost is None:
            return Response({"message": "Post is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        if str(findPost.user.id) != str(request.userId):
            return Response({"message": "You cannot update the post", "status": "403", "error": "True"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PostSerializers(findPost, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        findPostUser = User.objects.filter(id=request.userId).first()
        serializer.save(user=findPostUser)

        print(request.userId)
        return Response({"message": "Post is update", "status": "200", "error": "False"},status=status.HTTP_200_OK)
    
    
class Delete(APIView):
    def delete(self,request,pk):
        #find Post
        findPost=Post.objects.filter(id=pk).first()
        if findPost is None:
            return Response({"message": "Post is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        
        if str(findPost.user.id) != str(request.userId):
            return Response({"message": "You cannot Delete the post", "status": "403", "error": "True"}, status=status.HTTP_403_FORBIDDEN)
        Post.objects.filter(id=pk).delete()
        
        return Response({"message": "Post is Deleted", "status": "200", "error": "False"},status=status.HTTP_200_OK)
    
#create post like
class LikePost(APIView):
    
    def get(self,request,pk):
        
        # Find Post
        findPost = Post.objects.filter(id=pk).first()
        #find postLike
        findLikePost=PostLike.objects.filter(post=findPost)
        
        if findPost is None:
          return Response({"message": "Post is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostLikeSerializer(findLikePost, many=True)
        
        return Response({ "success": True, "likes_list": serializer.data })
    
    def post(self,request,pk):
        # Find Post
        findPost = Post.objects.filter(id=pk).first()
        #find user
        findUser =User.objects.filter(id=request.userId).first();
        if findPost is None:
          return Response({"message": "Post is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        new = PostLike.objects.get_or_create(user=findUser, post=findPost)
        
        if not new[1]:
                new[0].delete()
                return Response({ "success": True, "message": "post unliked" })
        else:
                return Response({ "success": True, "message": "post liked" })
        
        
#comment

class CommentPost(APIView):
    
    
    def post(self,request,pk):
        serializer = PostCommentSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Find Post
        findPost = Post.objects.filter(id=pk).first()
        
        #find User
        findUser = User.objects.filter(id=request.userId).first()
        
        if findPost is None:
          return Response({"message": "Post is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.save(post=findPost,user=findUser)
        return Response(serializer.data)
        
    def put(self,request,pk):
        #find comment
        findComment = PostComment.objects.filter(id=pk).first()
        if findComment is None:
            return Response({"message": "Comment is not found", "status": "404", "error": "True"}, status=status.HTTP_404_NOT_FOUND)
        if str(findComment.user.id)!=str(request.userId):
             return Response({"message": "you can not update comment", "status": "403", "error": "True"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer=PostCommentSerialize(findComment,data=request.data,partial=True)
     
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
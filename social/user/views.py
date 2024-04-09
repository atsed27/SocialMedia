
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer,FollowSerializer
from rest_framework import status
from .models import User,UserFollow
import jwt, datetime


import bcrypt



# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #Get password from serializer
        password = serializer.validated_data.get('password')
        
        #hash password
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Update the serializer data with the hashed password
        serializer.validated_data['password'] = hashed_password.decode('utf-8')
       
        #save
        serializer.save()
        return Response(serializer.data)


#Login class

class LoginView(APIView):
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print(email, password)

        # Find user by Email
        findUser = User.objects.filter(email=email).first()

        print(findUser is None)
        print(findUser)

        if findUser is None:
            return Response("User is not found", status=status.HTTP_404_NOT_FOUND)

        # Compare the provided password with the hashed password
        checkPassword = bcrypt.checkpw(password.encode('utf-8'), findUser.password.encode('utf-8'))

        print(checkPassword)

        if not checkPassword:
            return Response(
                {"message": "Password is incorrect", "status": "409", "error": "True"},
                status=status.HTTP_409_CONFLICT,
            )

        # Create Jwt Token
        payload = {
            'id': str(findUser.id),  # Convert UUID to string
            'isAdmin':str(findUser.is_superuser),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='ene', value=token, httponly=True)
        
        # Serialize the user object
        serializer = UserSerializer(findUser)
        
        response.data = serializer.data
        return response


#Test Token
class GetUser(APIView):
    def get(self,request):
        print(request.userId)
        findUser = User.objects.filter(id=request.userId).first()
        
        print(findUser)
        # Serialize the user object
        serializer = UserSerializer(findUser)
        return Response(serializer.data)

class Follower(APIView):
    def post(self,request,pk):
        #find user
        findUser=User.objects.filter(id=pk).first();
        
        #find signIn user
        signInUser=User.objects.filter(id=request.userId).first()
        
        if findUser is None:
            return Response("User is not found", status=status.HTTP_404_NOT_FOUND)
        
        print(findUser.id)
        if str(findUser.id) == str(request.userId):
            return Response("you are not follow yourSelf", status=status.HTTP_409_CONFLICT)
        
        followUser = UserFollow.objects.get_or_create(user=signInUser,follows=findUser)
        following = UserFollow.objects.get_or_create(user=findUser,following=signInUser)
        if not followUser[1]:
                followUser[0].delete()
                return Response({ "success": True, "message": "unFollowed user" },status=status.HTTP_202_ACCEPTED)
        else:
                return Response({ "success": True, "message": "followed user" },status=status.HTTP_202_ACCEPTED)


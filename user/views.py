
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User



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




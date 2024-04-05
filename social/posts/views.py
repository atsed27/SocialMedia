from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers
from user.models import User

# Create your views here.

class Create(APIView):
    
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        findUser = User.objects.filter(id=request.userId).first()

        #save
        serializer.save(user=findUser)
        
        return Response(serializer.data)
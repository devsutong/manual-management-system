from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Item
from .serializers import ItemSerializer

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    
    def get(self, request, *args, **kwargs):
        pass

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'brand_name': request.data.get('brand_name'), 
            'model_name': request.data.get('model_name'), 
            'manufacturer': request.data.get('manufacturer'),
            'manual': request.data.get('manual'),
            'drawing': request.data.get('drawing'),
            'qrcode': request.data.get('qrcode')
        }
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
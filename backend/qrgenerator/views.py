from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Item
from .serializers import ItemSerializer

import qrcode
import random
from django.core.files import File 
import urllib

class ItemApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # def qr_code_generator(brand_name, model_name, manufacturer, manual, drawing, qrcode):
    #     pass
    
    def get(self, request, *args, **kwargs):
        return Response("Working")

    # 2. Create
    def post(self, request, *args, **kwargs):
        # data = {
        #     'brand_name': request.data.get('brand_name'), 
        #     'model_name': request.data.get('model_name'), 
        #     'manufacturer': request.data.get('manufacturer'),
        #     'manual': request.data.get('manual'),
        #     'drawing': request.data.get('drawing'),
        #     'qrcode': request.data.get('qrcode')
        # }
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=4,
            )

            s = "http://127.0.0.1:8000/products/" + request.data
            qr.add_data(s)
            qr.make(fit=True)
            # qrPath = 'mystatic/media/' + qrName + '.png'
            img = qr.make_image(fill_color="black", back_color="white")
            img.save('mystatic/media/' + random.randint(0, 999) + '.png')
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['brand_name', 'model_name', 'manufacturer', 'manual', 'drawing']

class GenerateSerializer(serializers.Serializer):
    text = serializers.CharField(required = True)
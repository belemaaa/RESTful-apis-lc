from rest_framework import serializers
from .models import Product

class ProductSerialzer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'email',
            'title',
            'content',
            'price',
            'sale_price'
        ]
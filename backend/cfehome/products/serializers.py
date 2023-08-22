from rest_framework import serializers
from .models import Product

class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price'
        ]
    
    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already exists.")
        return value
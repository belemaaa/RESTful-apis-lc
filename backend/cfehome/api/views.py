import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerialzer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerialzer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)

        return Response(serializer.data)

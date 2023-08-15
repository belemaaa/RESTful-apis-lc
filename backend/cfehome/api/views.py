import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerialzer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance)
        data = ProductSerialzer(instance).data
    return Response(data)

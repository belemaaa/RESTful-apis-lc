from rest_framework import generics
from rest_framework import authentication
from .models import Product
from .serializers import ProductSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffPermission
from api.authentication import TokenAuthentication



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication]
    permission_classes = [IsStaffPermission]

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    lookup_field= 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    lookup_field= 'pk'
    
    def perform_delete(self, instance):
        super().perform_destroy(instance)




# create, retrieve and list - using functions
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerialzer(obj, many=False).data
            return Response(data)

        #list view
        qs = Product.objects.all()
        data = ProductSerialzer(qs, many=True).data
        return Response(data)

    if request.method == "POST":
        serializer = ProductSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
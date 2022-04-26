from rest_framework import generics
from api.models.products import Product
from api.serializers.products import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.visible_objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

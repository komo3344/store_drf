from rest_framework import generics
from api.models.products import Product, ProductOption
from api.serializers.products import ProductListSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

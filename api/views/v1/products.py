from rest_framework import generics
from api.models.products import Product, ProductOption


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()

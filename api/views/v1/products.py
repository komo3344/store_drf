from rest_framework import generics
from api.models.products import Product
from api.serializers.products import ProductSerializer

from drf_spectacular.views import extend_schema


@extend_schema(tags=['상품'], summary='숨김 상품을 제외한 제품 리스트')
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.visible_objects.all()    # 숨김 상품을 제외한 리스트
    serializer_class = ProductSerializer


@extend_schema(tags=['상품'], summary='상품 상세 정보')
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django.urls import path
from api.views.v1 import products as v1_products

app_name = 'api'

urlpatterns = [
    # 상품
    path('v1/product', v1_products.ProductListAPIView.as_view(), name='list'),
    path('v1/product/<int:pk>', v1_products.ProductDetailAPIView.as_view(), name='detail'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api.views.v1 import products as v1_products

app_name = 'api'

urlpatterns = [
    # 상품
    path('v1/product', v1_products.ProductListAPIView.as_view(), name='list'),
    path('v1/product/<int:pk>', v1_products.ProductDetailAPIView.as_view(), name='detail'),

    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]

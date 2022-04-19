from django.urls import path
from api.views.v1 import products as v1_products

app_name = 'api'

urlpatterns = [
    path('v1/product', v1_products.ProductListAPIView.as_view()),
]

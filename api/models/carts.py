from django.db import models
from core import models as core_models


class Cart(core_models.DateTimeModel):
    user = models.OneToOneField('api.User', on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey('api.Product', on_delete=models.SET_NULL, null=True, related_name='carts')
    variant = models.ForeignKey('api.ProductVariant', on_delete=models.SET_NULL, null=True, related_name='carts')


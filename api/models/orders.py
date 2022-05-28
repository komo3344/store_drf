import uuid

from django.db import models
from core import models as core_models


class Order(core_models.DateTimeModel):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('api.User', on_delete=models.CASCADE, related_name='orders')
    # 배송지
    # 결제수단
    # 주문일시 (created_at)
    # 결제금액 FK (결제수단명)


class OrderHistory(core_models.DateTimeModel):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('api.Product', on_delete=models.SET_NULL, null=True, related_name='order_histories')
    variant = models.ForeignKey('api.ProductVariant', on_delete=models.SET_NULL, null=True, related_name='order_histories')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

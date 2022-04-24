from django.db import models
from core import models as core_models


class Product(core_models.DateTimeModel):
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)     # 상품 정가
    is_sold_out = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    main_image = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = '상품'

    def __str__(self):
        return self.name


class ProductVariant(core_models.DateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    add_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)     # 상품 정가
    quantity = models.PositiveIntegerField(default=0)
    is_sold_out = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '상품 세부품목'


class ProductOption(core_models.DateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = '상품 옵션'


class ProductOptionVariation(core_models.DateTimeModel):
    option = models.ForeignKey('ProductOption', on_delete=models.CASCADE, related_name='variations')
    value = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = '상품 값'


class ProductImage(core_models.DateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

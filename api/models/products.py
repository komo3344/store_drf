from django.db import models
from core import models as core_models


# 상품
class Product(core_models.VisibleDateTimeModel):
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)     # 상품 정가
    is_sold_out = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    main_image = models.ImageField(null=True, blank=True, upload_to='products/%Y/%m/%d/')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = '상품'

    def __str__(self):
        return self.name


# 세부 품목(실물)
class ProductVariant(core_models.VisibleDateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    add_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)     # 상품 정가
    quantity = models.PositiveIntegerField(default=0)
    is_sold_out = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '상품 세부품목'

    def __str__(self):
        return f'{self.product.name} (세부품목)'


# 상품 옵션
class ProductOption(core_models.DateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = '상품 옵션'

    def __str__(self):
        return f'{self.name} ({self.id})'


# 상품 옵션 값
class ProductOptionVariation(core_models.DateTimeModel):
    option = models.ForeignKey('ProductOption', on_delete=models.CASCADE, related_name='variations')
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, null=True, related_name='variations')
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

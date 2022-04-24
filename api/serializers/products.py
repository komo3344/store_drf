from rest_framework import serializers

from api.models.products import Product, ProductOption, ProductOptionVariation, ProductVariant


# 기본 상품
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'main_image',
            'is_sold_out', 'is_hidden', 'is_delete',
        ]


# 기본 상품 옵션
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['product', 'name']


# 기본 상품 옵션 값
class ProductOptionVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionVariation
        fields = ['value']


# 기본 상품 세부품목
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['product', 'add_price', 'quantity', 'is_sold_out', 'is_hidden']


# 상품 리스트
class ProductListSerializer(ProductSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ProductSerializer.Meta.fields + [
            'variants'
        ]

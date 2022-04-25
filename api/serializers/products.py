from rest_framework import serializers

from api.models.products import Product, ProductOption, ProductOptionVariation, ProductVariant


# 기본 상품
class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'main_image',
            'is_sold_out', 'is_hidden', 'is_delete',
        ]


# 기본 상품 옵션
class BaseProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['product', 'name']


# 기본 상품 옵션 값
class BaseProductOptionVariationSerializer(serializers.ModelSerializer):
    option_name = serializers.CharField(source='option.name')

    class Meta:
        model = ProductOptionVariation
        fields = ['value', 'option_name']


# 기본 상품 세부품목 + 옵션 값
class BaseProductVariantSerializer(serializers.ModelSerializer):
    variations = BaseProductOptionVariationSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'add_price', 'quantity', 'is_sold_out', 'is_hidden', 'variations']


class ProductSerializer(BaseProductSerializer):
    variants = BaseProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = BaseProductSerializer.Meta.fields + [
            'variants'
        ]


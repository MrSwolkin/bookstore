from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializers


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializers(required=True, many=True)
    total = serializers.serializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model: Product
        fields: ['product', 'total']

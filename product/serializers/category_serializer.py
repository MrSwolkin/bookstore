from rest_framework import serializers

from product.models.category import Category


class CategorySerializers(serializers.ModelsSerializer):
    class Meta:
        models = Category
        fields = [
            'title',
            'slug',
            'description',
            'active'
        ]

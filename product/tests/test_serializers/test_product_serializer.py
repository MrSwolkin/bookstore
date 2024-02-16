from django.test import TestCase

from product.factories import ProductFactory
from product.factories import CategoryFactory

from product.serializers import ProductSerializer


class TesteProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title='office')
        self.product_1 = ProductFactory(title='pen', category=[self.category])
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data['title'], 'pen')
        self.assertEqual(serializer_data['category'][0]['title'], 'office')

# importando o django teste
from django.test import TestCase

# importando os factorries
from product.factories import ProductFactory
from product.factories import CategoryFactory

# importando o serializer de categorias
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title='teste1')
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEqual(serializer_data['title'], self.category.title)

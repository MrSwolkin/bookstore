from django.test import TestCase

from product.models import Product, Category


class TestProductModels(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='testando', slug='teste_slug')
        self.product = Product.objects.create(title='produto_test')
        self.product.category.add(self.category)


def test_product_creation(self):
    self.assertEqual(self.product.title, 'produto_test')
    self.assertEqual(self.product.category[0]['title'], 'testando')

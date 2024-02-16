# importando o django teste -  testCase
from django.test import TestCase
from django.contrib.auth.models import User


# importando nosso model order
from order.models import Order
# importando o product
from product.models import Product


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='test_name')
        self.product_1 = Product.objects.create(title='produto_1')

    def test_order(self):
        order = Order.objects.create(user=self.user)
        order.product.add(self.product_1)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.product.first().title, self.product_1.title)

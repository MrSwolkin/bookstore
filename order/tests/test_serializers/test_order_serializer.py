from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        # Cria dois produtos usando a fábrica de produtos
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()
        # Cria um pedido associado a esses produtos usando a fábrica de pedidos
        self.order = OrderFactory(product=(self.product_1, self.product_2))
        # Instancia o serializador de pedido com o pedido criado
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        # Verifica se os títulos dos produtos no pedido serializado correspondem aos títulos dos produtos criados
        serializer_data = self.order_serializer.data
        self.assertEqual(
            serializer_data['product'][0]['title'], self.product_1.title)
        self.assertEqual(
            serializer_data['product'][1]['title'], self.product_2.title)

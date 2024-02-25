# importando o json
import json
# importando o status e a biblioteca de teste do rest_framework
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse
# importando bibliotecas do app
from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory, OrderFactory
from product.models import Product
from order.models import Order

# definido classe de test


class TestOrderViewSet(APITestCase):

    # configurando cliente da API
    client = APIClient()

    # configurando os dados de teste
    def setUp(self):
        # criando categoria do produto
        self.category = CategoryFactory(title='tecnology')
        # criando produto assiciado a categoria
        self.product = ProductFactory(
            title='mouse', price=100, category=[self.category])
        # crinado uma ordem de pedido do produto criado
        self.order = OrderFactory(product=[self.product])

    # testando a listagem de pedidos
    def test_order(self):
        # solicitando com GET  para listar os pedidos
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )
        # verificando se a resposta fo bem-sucedida (status 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # analisando dados da resposta JSON
        order_data = json.loads(response.content)

        # comparando dados do pedido com o dados do produto e categoria
        self.assertEqual(order_data['results'][0]
                         ['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['results'][0]
                         ['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['results'][0]['product'][0]
                         ['active'], self.product.active)
        self.assertEqual(order_data['results'][0]['product'][0]
                         ['category'][0]['title'], self.category.title)

    # testando criação de um novo pedido
    def test_create_order(self):
        # criando usuario de teste
        user = UserFactory()

        # criando um produto de teste
        product = ProductFactory()

        # criando os dados do pedido em formato json
        data = json.dumps({
            # id do produto incluido no pedido
            'products_id': [product.id],
            'user': user.id  # id do usuario que fez o pedido
        })
        # fazendo uma solicitaçõa POST para criar um novo pedido
        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        # verificando se foi bem-sucesdida (código staus:201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(Order.objects.get(user=user))
        # buscando o pedido recém-criado no banco de dados
        created_order = Order.objects.get(user=user)

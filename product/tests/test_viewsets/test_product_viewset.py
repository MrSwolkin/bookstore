# importando as bibliotecas necessarias
import json

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models import Product

# craindo a classe teste


class TestProductViewset(APITestCase):
    # coniguranod o client de API para os testes
    client = APIClient()

    def setUp(self):
        # criando um usuario de teste
        self.user = UserFactory()

        # crinado um produto de teste
        self.product = ProductFactory(
            title='pro-controller',
            price=200.00,
        )

    def test_get_all_product(self):

        # testando o resultado dos produtos obtidos através da API
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )
        # verificando se a resposta foi bem-sucedida (code status 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # dados do produto retornado pela API amazenado na variavel product_data
        product_data = json.loads(response.content)

        # compoarando os dados obtido da api com o do produto de teste
        self.assertEqual(product_data['results']
                         [0]['title'], self.product.title)
        self.assertEqual(product_data['results']
                         [0]['price'], self.product.price)
        self.assertEqual(product_data['results']
                         [0]['active'], self.product.active)

    def test_create_product(self):

        # crinado a categoria para associar ao produto novo
        category = CategoryFactory()

        # Criando os dados do novo produto em json
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories_id': [category.id]
        })

        # print('data:', data)
        # fazendo a solicitação de POST para a criar um novo produto na API
        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        # verifianco se a criação foi bem-sucedida codigo status 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print('response:', response.status_code, response.content)

        # buscando no banco de dados o recém criado produto pelo titulo
        created_product = Product.objects.get(title='notebook')

        # verificando se os dados do produto correspodem aos fornencidos pelo banco de dados
        self.assertEqual(created_product.title, 'notebook')
        self.assertEqual(created_product.price, 800.00)

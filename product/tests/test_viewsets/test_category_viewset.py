# importando as bibliotecas necessárias
import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from product.models import Category

# criando a classe de teste


class TestCategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # criando uma categoria de produto
        self.category = CategoryFactory(title="books")

    def test_get_all_category(self):
        # testando u resultado da categoria dentro da api
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))
        # import pdb; pdb.set_trace()
        # varificando se a resposta foi 200 + a bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # dados de category retornado pela api

        category_data = json.loads(response.content)

        self.assertEqual(category_data["results"][0]["title"], self.category.title)

    def test_create_category(self):
        # criando um nova categoria em json
        data = json.dumps({"title": "technology"})

        # PoST para criar uma nova categoria na API
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # comparando se a resposta retornada é bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # buscando no banco de dados a categoria recem criada
        created_category = Category.objects.get(title="technology")

        # comparando
        self.assertEqual(created_category.title, "technology")

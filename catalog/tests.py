from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from catalog.models import Product, Category


class CategoryTests(APITestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='All', description='All')
        self.category2 = Category.objects.create(name='Smartphones', description='Smartphones')

    def test_get_category(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # self.assertEqual(set([c.name for c in response.data]), {self.category1.name, self.category2.name})


class ProductTests(APITestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='All', description='All')
        self.category2 = Category.objects.create(name="Xiaomi", description="Дишманские телефоны")

        self.product1 = Product.objects.create(name='Xiaomi', price=101, special_price=90)
        self.product1.category.add(self.category1)
        self.product1.category.add(self.category2)

    def test_get_product(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('product-list')
        id1 = str(self.category1.id)
        id2 = str(self.category2.id)
        response = self.client.get(url + '?category=' + id1 + ',' + id2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.product1.id)

    def test_product_price_filter(self):
        url = reverse('product-list')
        response = self.client.get(url + '?price=10-5', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

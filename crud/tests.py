# apps/crud/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Customer, Product

class CustomerTests(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="Pedro",
            last_name="Osorio",
            email="pedro@example.com",
            phone="+56912345678"
        )
        self.customer_url = reverse('customer-list')  # Usa el nombre del router DRF

    def test_create_customer(self):
        data = {
            "first_name": "Juan",
            "last_name": "Perez",
            "email": "juan@example.com",
            "phone": "+56987654321"
        }
        response = self.client.post(self.customer_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.get(email="juan@example.com").first_name, "Juan")

    def test_list_customers(self):
        response = self.client.get(self.customer_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_email_unique(self):
        data = {
            "first_name": "Pedro",
            "last_name": "Osorio",
            "email": "pedro@example.com"
        }
        response = self.client.post(self.customer_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ProductTests(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Libro Django",
            description="Curso completo",
            price=25000,
            stock=10
        )
        self.product_url = reverse('product-list')

    def test_create_product(self):
        data = {
            "name": "Libro Python",
            "description": "Guía avanzada",
            "price": 30000,
            "stock": 5
        }
        response = self.client.post(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(name="Libro Python").price, 30000)

    def test_list_products(self):
        response = self.client.get(self.product_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_stock_non_negative(self):
        data = {
            "name": "Libro Test",
            "description": "Stock negativo",
            "price": 1000,
            "stock": -5
        }
        response = self.client.post(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

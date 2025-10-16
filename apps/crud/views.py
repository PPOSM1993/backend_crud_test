from django.shortcuts import render
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer
from rest_framework import viewsets
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
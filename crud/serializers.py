# apps/crud/serializers.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Customer, Product
import re

# -------------------------
# Customer Serializer
# -------------------------
class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    phone = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_phone(self, value):
        """Validar que el teléfono tenga formato numérico (opcional + o espacios)"""
        if value and not re.match(r'^\+?\d{7,15}$', value):
            raise serializers.ValidationError("Número de teléfono inválido. Debe contener entre 7 y 15 dígitos, opcional prefijo +")
        return value

    def validate_first_name(self, value):
        return value.strip().capitalize()

    def validate_last_name(self, value):
        return value.strip().capitalize()


# -------------------------
# Product Serializer
# -------------------------
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=200,
        required=True,
        validators=[UniqueValidator(queryset=Product.objects.all())]
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01
    )
    stock = serializers.IntegerField(
        min_value=0
    )
    description = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at']
        read_only_fields = ['id']

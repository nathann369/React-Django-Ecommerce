from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product
from .models import Address
from .models import Category
from .models import Cart

# for user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "fullname", "email", "password","phone","address","zip-code"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

# for product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "product_name", "price", "description", "created_at"]

    def create(self, validated_data):
        print(validated_data)
        product = Product.objects.create(**validated_data)
        return product

# for address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "user_id", "address", "country", "phone"]

    def create(self, validated_data):
        print(validated_data)
        address = Address.objects.create(**validated_data)
        return address

# for cart
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "product_id", "quantity", "created_at"]

    def create(self, validated_data):
        print(validated_data)
        cart = Cart.objects.create(**validated_data)
        return user

# for category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "created_at"]

    def create(self, validated_data):
        print(validated_data)
        category = Category.objects.create(**validated_data)
        return category
      
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ProductSerializer, AddressSerializer, CartSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Product, Address, Cart, Category

# Create your views here.

# Creating a new product
class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# deleting product
class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.all()


# Creating a new Address
class AddressCreate(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.all()

# deleting a address        
class AddressDelete(generics.DestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.all()

   


# Creating a new Cart
class CartItemsCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.all()

# deleting cart        
class CartDelete(generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.all()

    
 
 # Creating a new Category
class CategoryListCreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.all()

# deleting Category        
class CategoryDelete(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.all()
 

# creating user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
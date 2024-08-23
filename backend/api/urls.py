from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListCreate.as_view(), name="product-list"),
    path("products/delete/<int:pk>/", views.ProductDelete.as_view(), name="delete-product"),
    path("carts/", views.CartItemsCreate.as_view(), name="cart-list"),
    path("carts/delete/<int:pk>/", views.CartDelete.as_view(), name="delete-cart"),
    path("categorys/", views.CategoryListCreate.as_view(), name="category-list"),
    path("categorys/delete/<int:pk>/", views.CategoryDelete.as_view(), name="delete-category"),
    path("address/", views.AddressCreate.as_view(), name="address-list"),
    path("address/delete/<int:pk>/", views.AddressDelete.as_view(), name="delete-address"),
]
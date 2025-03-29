from django.urls import path
from api import views

urlpatterns = [
    path("products/", views.products),
    path("products/<int:id>/", views.product),
    path("categories/", views.categories),
    path("categories/<int:id>", views.category),
    path("categories/<int:id>/products", views.products_by_category)
]
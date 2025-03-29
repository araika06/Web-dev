from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse
from django.http import Http404

def products(request):
    products = Product.objects.all()
    result = []
    for product in products:
        result.append(product.to_json())
    return JsonResponse(result, safe=False)

def product(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product.to_json())
    except Product.DoesNotExist:
        raise Http404("Product not found")

def categories(request):
    categories = Category.objects.all()
    result = []
    for category in categories:
        result.append(category.to_json())
    return JsonResponse(result, safe=False)

def category(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category.to_json())
    except Product.DoesNotExist:
        raise Http404("Category not found")

def products_by_category(request, id):
    products = Product.objects.filter(category_id = id)
    result = []
    for product in products:
        result.append(product.to_json())
    return JsonResponse(result, safe=False)

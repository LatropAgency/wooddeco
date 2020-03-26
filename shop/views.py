from django.shortcuts import render
from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def product_category(request,slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request,'index.html',{'categories': categories,'products':products})
from django.shortcuts import render, get_object_or_404
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

def more_info(request,id):
    tupl = get_object_or_404(Product, id=id)
    more_info = {'more_info': tupl}
    return render(request, 'more_info.html', more_info)

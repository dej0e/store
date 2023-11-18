from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def aboutPage(request):
    return render(request, 'about.html')


# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/detail.html', {'product': product})

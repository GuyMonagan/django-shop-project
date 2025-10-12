from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'latest_products': latest_products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

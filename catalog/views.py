from django.shortcuts import render
from .models import Product

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'latest_products': latest_products})

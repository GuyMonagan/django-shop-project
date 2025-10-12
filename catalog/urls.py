from django.urls import path
from catalog.views import ProductDetailView
from catalog.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

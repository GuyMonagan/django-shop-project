from django.contrib import admin
from .models import Category, Product, ContactData

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover;" />',
                obj.image.url
            )
        return "Нет изображения"

    image_preview.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

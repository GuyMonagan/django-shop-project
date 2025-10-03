from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Загружает тестовые данные из фикстур"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загружаем новые данные из фикстуры...")
        call_command('loaddata', 'catalog/fixtures/initial_data.json')

        self.stdout.write(self.style.SUCCESS("✅ Тестовые данные успешно загружены."))

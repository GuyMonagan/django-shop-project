from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Создаёт группы и раздаёт права"

    def handle(self, *args, **kwargs):
        mod_group, created = Group.objects.get_or_create(name="Модератор продуктов")
        content_type = ContentType.objects.get_for_model(Product)

        perms = [
            Permission.objects.get(codename='delete_product', content_type=content_type),
            Permission.objects.get(codename='can_unpublish_product', content_type=content_type),
        ]

        mod_group.permissions.set(perms)
        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и настроена.'))

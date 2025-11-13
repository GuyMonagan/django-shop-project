from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создаёт группы с правами"

    def handle(self, *args, **kwargs):
        # Группа модераторов продуктов
        moderators_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write('Группа "Модератор продуктов" создана.')
        else:
            self.stdout.write('Группа "Модератор продуктов" уже существует.')

        # Права для модераторов продуктов
        delete_product = Permission.objects.get(codename='delete_product')
        can_unpublish = Permission.objects.get(codename='can_unpublish_product')
        moderators_group.permissions.set([delete_product, can_unpublish])

        # Группа контент-менеджеров
        content_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        if created:
            self.stdout.write('Группа "Контент-менеджер" создана.')
        else:
            self.stdout.write('Группа "Контент-менеджер" уже существует.')

        # Права для блога (добавь нужные, если кастомные есть)
        blog_permissions = Permission.objects.filter(content_type__app_label='blog')
        content_group.permissions.set(blog_permissions)

        self.stdout.write(self.style.SUCCESS('Группы настроены!'))

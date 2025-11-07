from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # 🔥 Восстанавливаем username, но убираем его как auth-поле
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    country = models.CharField(max_length=50, blank=True, verbose_name="Страна")

    USERNAME_FIELD = 'email'  # авторизация по email
    REQUIRED_FIELDS = ['username']  # чтобы django просил username при createsuperuser

    objects = CustomUserManager()

    def __str__(self):
        return self.username  # 👈 вот тут теперь будет MikroNagibator2000

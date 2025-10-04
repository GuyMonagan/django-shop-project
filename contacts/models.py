from django.db import models


class ContactData(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя и статус")
    value = models.CharField(max_length=255, verbose_name="Адрес, номер, email и т.п.)")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name}: {self.value}"


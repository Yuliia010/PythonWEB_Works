from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    specialization = models.CharField(max_length=100, verbose_name="Спеціалізація")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    website = models.URLField(blank=True, null=True, verbose_name="Веб-сайт")
    phone = models.CharField(max_length=20, verbose_name="Контактний телефон")

    def __str__(self):
        return self.name
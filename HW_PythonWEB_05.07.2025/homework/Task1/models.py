from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Seller(models.Model):
    POSITION_CHOICES = [
        ('seller', 'Продавец'),
        ('senior', 'Старший продавец'),
        ('manager', 'Руководитель отдела продаж'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    hire_date = models.DateField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.get_position_display()})'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.amount} грн'

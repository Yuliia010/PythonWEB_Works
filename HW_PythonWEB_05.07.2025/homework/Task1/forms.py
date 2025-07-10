from django import forms
from Task1.models import Customer, Product, Seller


class CustomerForm(forms.Form):
    first_name = forms.CharField(label='Ім’я')
    last_name = forms.CharField(label='Прізвище')
    phone = forms.CharField(label='Телефон')
    email = forms.EmailField(label='Email')

class SellerForm(forms.Form):
    POSITION_CHOICES = [
        ('seller', 'Продавець'),
        ('senior', 'Старший продавець'),
        ('manager', 'Руководитель відділу продажів'),
    ]
    first_name = forms.CharField(label='Ім’я')
    last_name = forms.CharField(label='Прізвище')
    phone = forms.CharField(label='Телефон')
    email = forms.EmailField(label='Email')
    hire_date = forms.DateField(label='Дата прийому на роботу', widget=forms.DateInput(attrs={'type': 'date'}))
    position = forms.ChoiceField(label='Посада', choices=POSITION_CHOICES)

class ProductForm(forms.Form):
    name = forms.CharField(label='Назва товару')
    description = forms.CharField(label='Опис', widget=forms.Textarea)

class SaleForm(forms.Form):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        label='Покупець',
        empty_label="Оберіть покупця"
    )
    seller = forms.ModelChoiceField(
        queryset=Seller.objects.all(),
        label='Продавець',
        empty_label="Оберіть продавця"
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label='Товар',
        empty_label="Оберіть товар"
    )
    sale_date = forms.DateField(label='Дата продажу', widget=forms.DateInput(attrs={'type': 'date'}))
    amount = forms.DecimalField(label='Сума продажу', min_value=0, decimal_places=2)



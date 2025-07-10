from django import forms

class RestaurantForm(forms.Form):
    name = forms.CharField(label='Назва', max_length=255)
    specialization = forms.CharField(label='Спеціалізація', max_length=100)
    address = forms.CharField(label='Адреса', max_length=255)
    website = forms.URLField(label='Веб-сайт', required=False)
    phone = forms.CharField(label='Телефон', max_length=20)

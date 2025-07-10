"""
URL configuration for homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Task1.views import add_customer, add_product, add_sale, add_seller, customer_list, home, product_list, sale_list, seller_list

urlpatterns = [
    path('', home, name='home'),
    path('customers/', customer_list, name='customer_list'),
    path('sellers/', seller_list, name='seller_list'),
    path('products/', product_list, name='product_list'),
    path('sales/', sale_list, name='sale_list'),

    path('customers/add/', add_customer, name='add_customer'),
    path('sellers/add/', add_seller, name='add_seller'),
    path('products/add/', add_product, name='add_product'),
    path('sales/add/', add_sale, name='add_sale'),
]

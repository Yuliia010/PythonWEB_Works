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
from Task1.views import add_restaurant, delete_restaurant, edit_restaurant, restaurant_list


urlpatterns = [
    path('', restaurant_list, name='restaurant_list'),
    path('add/', add_restaurant, name='add_restaurant'),
    path('delete/<int:restaurant_id>/', delete_restaurant, name='delete_restaurant'),
    path('edit/<int:restaurant_id>/', edit_restaurant, name='edit_restaurant'),
]

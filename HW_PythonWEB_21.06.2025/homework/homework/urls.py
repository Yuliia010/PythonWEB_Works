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
from django.urls import path, re_path
from Task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('writers/', views.writers, name='writers'),
    path('writers/<str:writer_name>/', views.writer_detail, name='writer_detail'),
    path('books/', views.books, name='books'),
    path('books/<int:book_rank>/', views.book_detail, name='book_detail'),
    path('writers/<str:writer_name>/<str:book_slug>/', views.writer_book_detail, name='writer_book_detail'),
]

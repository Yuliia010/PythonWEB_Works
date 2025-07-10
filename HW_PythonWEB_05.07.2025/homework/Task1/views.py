from django.shortcuts import get_object_or_404, redirect, render
from Task1.forms import CustomerForm, ProductForm, SaleForm, SellerForm
from .models import Customer, Seller, Product, Sale

# Create your views here.
def home(request):
    return render(request, 'Task1/home.html')

def customer_list(request):
    return render(request, 'Task1/customers.html', {'customers': Customer.objects.all()})

def seller_list(request):
    return render(request, 'Task1/sellers.html', {'sellers': Seller.objects.all()})

def product_list(request):
    return render(request, 'Task1/products.html', {'products': Product.objects.all()})

def sale_list(request):
    return render(request, 'Task1/sales.html', {'sales': Sale.objects.all()})

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        Customer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email']
        )
        return redirect('customer_list')
    return render(request, 'Task1/add_customer.html', {'form': form})

def add_seller(request):
    form = SellerForm(request.POST or None)
    if form.is_valid():
        Seller.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            hire_date=form.cleaned_data['hire_date'],
            position=form.cleaned_data['position']
        )
        return redirect('seller_list')
    return render(request, 'Task1/add_seller.html', {'form': form})

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        Product.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description']
        )
        return redirect('product_list')
    return render(request, 'Task1/add_product.html', {'form': form})

def add_sale(request):
    form = SaleForm(request.POST or None)
    if form.is_valid():
        Sale.objects.create(
            customer=form.cleaned_data['customer'],
            seller=form.cleaned_data['seller'],
            product=form.cleaned_data['product'],
            sale_date=form.cleaned_data['sale_date'],
            amount=form.cleaned_data['amount']
        )
        return redirect('sale_list')
    return render(request, 'Task1/add_sale.html', {'form': form})
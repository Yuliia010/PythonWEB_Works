from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect
from Task1.models import Restaurant
from .forms import RestaurantForm

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'Task1/restaurant_list.html', {'restaurants': restaurants})


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            specialization = form.cleaned_data['specialization']
            address = form.cleaned_data['address']
            website = form.cleaned_data['website']
            phone = form.cleaned_data['phone']

            Restaurant.objects.create(
                name=name,
                specialization=specialization,
                address=address,
                website=website,
                phone=phone
            )

            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'Task1/add_restaurant.html', {'form': form})

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == "POST":
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'Task1/delete_restaurant.html', {'restaurant': restaurant})

def edit_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant.name = form.cleaned_data['name']
            restaurant.specialization = form.cleaned_data['specialization']
            restaurant.address = form.cleaned_data['address']
            restaurant.website = form.cleaned_data['website']
            restaurant.phone = form.cleaned_data['phone']
            restaurant.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(initial={
            'name': restaurant.name,
            'specialization': restaurant.specialization,
            'address': restaurant.address,
            'website': restaurant.website,
            'phone': restaurant.phone,
        })
    return render(request, 'Task1/edit_restaurant.html', {'form': form, 'restaurant': restaurant})


def restaurant_list(request):
    query = request.GET.get('q', '') 
    if query:
        restaurants = Restaurant.objects.filter(specialization__icontains=query)
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'Task1/restaurant_list.html', {'restaurants': restaurants, 'query': query})

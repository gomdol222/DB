from django.shortcuts import render, redirect
from forms import MenuForm  
from restaurant.models import Menu 

def restaurant_account(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_account')

    else:
        form = MenuForm()

    menus = Menu.objects.all() 

    return render(request, 'restaurant_account.html', {'form': form, 'menus': menus})


from django.shortcuts import redirect, render
from .models import Restaurant, Menu, Review, SuggestionBoard
from django.utils import timezone
from .forms import MenuForm

def home(request):
    today = timezone.now().date()
    restaurant_name = Restaurant.objects.all()
    menu = Menu.objects.filter(created_at=today)
    context = {
        'restaurant_name' : restaurant_name,
        'menus' : menu
    }
    return render(request, 'home.html', context)


def restaurant_detail(request, restaurant_id):
    restaurants = Restaurant.objects.get(id=restaurant_id)
    # rating = Review.objects.get(restaurant=restaurants)
    reviews = Review.objects.order_by('-created_at') # 이거 바꿈. 원래는 all()
    context = {
        'restaurants': restaurants,
        'reviews' : reviews,
        # 'rating' : rating,
        }
    return render(request, 'restaurant_detail.html', context)

def restaurant_review(request, restaurant_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', restaurant_id)
    else:
        form = RatingForm()

    rating = Restaurant.objects.all()
    
    reviews = Review.objects.all()
    context = {
        'rating': rating,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'restaurant_review.html', context)

def restaurant_account(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            restaurant_name=form.cleaned_data['restaurant']
            form.save()
            return redirect('restaurant:restaurant_account')
    else:
        form = MenuForm()
        
    return render(request, 'restaurant_account.html', {'form': form})

def home(request):
    return render(request, 'base.html')


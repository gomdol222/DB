from django.urls import path
from . import views


app_name = 'restaurant_account'

urlpatterns = [
    path('restaurant_account/', views.restaurant_account, name='restaurant_account'),
]


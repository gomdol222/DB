from django.db import models
from django.db.models import Avg
from django.utils import timezone


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    event = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.restaurant_name

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.menu_name
    

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class SuggestionBoard(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    post_content = models.TextField()
    
class RestaurantAccount(models.Model):
    date = models.DateField(default=timezone.now)
    items = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.items}"
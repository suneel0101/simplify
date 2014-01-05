from django.contrib import admin
from .models import (
    Restaurant, RestaurantVisit, MealRecipient)

admin.site.register(Restaurant)
admin.site.register(RestaurantVisit)
admin.site.register(MealRecipient)

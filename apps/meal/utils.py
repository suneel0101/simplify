import datetime
import random
from django.conf import settings
from django.core.mail import send_mail
from .models import RestaurantVisit, Restaurant, MealRecipient



def generate_fresh_recommendation():
    last_five_restaurant_ids = list(RestaurantVisit.objects
                             .order_by('-date')
                             .values_list('restaurant_id', flat=True)[:5])
    choices = list(Restaurant.objects.exclude(id__in=last_five_restaurant_ids))
    return random.choice(choices)

def log_recommendation(restaurant):
    RestaurantVisit.objects.create(restaurant=restaurant)

def send_message(message):
    send_mail("Lunch rec for today: {}".format(datetime.datetime.today().strftime("%m %d %Y")),
              message,
              "SimplifyIt <simplifyit@pennypackerlabs.com",
              ['xie1989@gmail.com', 'suneel0101@gmail.com'])


def send_recommendation(restaurant):
    message = "Enjoy lunch today at {}! Details: {}".format(
        restaurant.name,
        restaurant.yelp_url)
    send_message(message)

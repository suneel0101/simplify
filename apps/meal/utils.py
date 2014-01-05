import random
from django.conf import settings
from .models import RestaurantVisit, Restaurant, MealRecipient

from twilio.rest import TwilioRestClient


def generate_fresh_recommendation():
    last_five_restaurant_ids = list(RestaurantVisit.objects
                             .order_by('-date')
                             .values_list('restaurant_id', flat=True)[:5])
    choices = list(Restaurant.objects.exclude(id__in=last_five_restaurant_ids))
    return random.choice(choices)

def log_recommendation(restaurant):
    RestaurantVisit.objects.create(restaurant=restaurant)

def send_recommendation(restaurant):
    client = TwilioRestClient(
        settings.TWILIO_ACCOUNT,
        settings.TWILIO_TOKEN)
    for recipient in MealRecipient.objects.all():
        message = client.messages.create(to=recipient.phone,
                                         from_=settings.TWILIO_FROM,
                                         body="Enjoy lunch today at {}! Details: {}".format(
                                             restaurant.name,
                                             restaurant.yelp_url))

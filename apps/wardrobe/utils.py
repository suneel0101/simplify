import random
from django.conf import settings
from .models import (
    Pants,
    Shoes,
    Shirt,
    Outfit,
    WardrobeRecipient,
    OutfitWear,
)

from twilio.rest import TwilioRestClient


def generate_fresh_recommendation():
    # get the last five outfits
    last_five_outfit_ids = list(OutfitWear.objects.order_by('-date').values_list('outfit_id', flat=True)[:5])

    # get the pants and shirts and that were worn in the most recent two outfits
    pants_and_shirts_to_exclude = list(
        Outfit.objects.filter(id__in=last_five_outfit_ids[:2])
        .values_list('pants_id', 'shirt_id'))
    pants_to_exclude = [pair[0] for pair in pants_and_shirts_to_exclude]
    shirts_to_exclude = [pair[1] for pair in pants_and_shirts_to_exclude]

    # choose from the outfits which do not use pants and shirts
    # from the most recent two outfits
    # and which are not in the most recent five outfits
    choices = list(Outfit.objects.exclude(
        id__in=last_five_outfit_ids,
        pants__in=pants_to_exclude,
        shirt__in=shirts_to_exclude))
    return random.choice(choices)

def log_recommendation(outfit):
    OutfitWear.objects.create(outfit=outfit)

def send_recommendation(outfit):
    client = TwilioRestClient(
        settings.TWILIO_ACCOUNT,
        settings.TWILIO_TOKEN)
    for recipient in WardrobeRecipient.objects.all():
        message = client.messages.create(to=recipient.phone,
                                         from_=settings.TWILIO_FROM,
                                         body="Today's look: {} + {} + {}".format(
                                             outfit.shirt,
                                             outfit.pants,
                                             outfit.shoes))

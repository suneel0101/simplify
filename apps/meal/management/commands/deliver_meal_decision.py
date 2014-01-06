import datetime

from django.core.management.base import BaseCommand
from meal.utils import (
    generate_fresh_recommendation,
    log_recommendation,
    send_message,
    send_recommendation)


class Command(BaseCommand):

    def handle(self, *args, **options):
        weekday = datetime.datetime.now().weekday()
        if weekday in (5, 6):
            return
        elif weekday == 1:
            send_message("Free lunch at eBay today!")
        else:
            restaurant = generate_fresh_recommendation()
            log_recommendation(restaurant)
            send_recommendation(restaurant)

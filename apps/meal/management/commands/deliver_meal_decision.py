from django.core.management.base import BaseCommand
from meal.utils import (
    generate_fresh_recommendation,
    log_recommendation,
    send_recommendation)


class Command(BaseCommand):

    def handle(self, *args, **options):
        restaurant = generate_fresh_recommendation()
        log_recommendation(restaurant)
        send_recommendation(restaurant)

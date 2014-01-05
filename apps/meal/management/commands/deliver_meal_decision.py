import datetime
from django.core.management.base import BaseCommand
from .utils import (
    generate_fresh_recommendation,
    send_recommendation)


class Command(BaseCommand):

    def handle(self, *args, **options):
        restaurant = generate_fresh_recommendation()
        send_recommendation(restaurant)

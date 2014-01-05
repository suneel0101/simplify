from django.core.management.base import BaseCommand
from wardrobe.utils import (
    generate_fresh_recommendation,
    log_recommendation,
    send_recommendation)


class Command(BaseCommand):

    def handle(self, *args, **options):
        outfit = generate_fresh_recommendation()
        log_recommendation(outfit)
        send_recommendation(outfit)

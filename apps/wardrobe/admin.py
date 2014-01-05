from django.contrib import admin
from .models import (
    Pants, Shirt, Shoes, Outfit, OutfitWear,
    WardrobeRecipient)

admin.site.register(Pants)
admin.site.register(Shirt)
admin.site.register(Shoes)
admin.site.register(Outfit)
admin.site.register(OutfitWear)
admin.site.register(WardrobeRecipient)

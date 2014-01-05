from django.db import models

class Pants(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Shirt(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Shoes(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Outfit(models.Model):
    pants = models.ForeignKey('wardrobe.Pants')
    shirt = models.ForeignKey('wardrobe.Shirt')
    shoes = models.ForeignKey('wardrobe.Shoes')

    def __unicode__(self):
        return ",".join(
            self.pants.name,
            self.shirt.name,
            self.shoes.name)


class OutfitWear(models.Model):
    outfit = models.ForeignKey('wardrobe.Outfit')
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"{}: {}".format(
            unicode(self.outfit),
            self.date)

class WardrobeRecipient(models.Model):
    user = models.ForeignKey("auth.User")
    phone = models.CharField(max_length=12)

    def __unicode__(self):
        return self.user.username

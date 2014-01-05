from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    yelp_url = models.URLField(max_length=500)

    def __unicode__(self):
        return self.name


class RestaurantVisit(models.Model):
    restaurant = models.ForeignKey('meal.Restaurant')
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u"{}: {}".format(
            self.restaurant.name,
            self.date)


class MealRecipient(models.Model):
    user = models.ForeignKey("auth.User")
    phone = models.CharField(max_length=12)

    def __unicode__(self):
        return self.user.username

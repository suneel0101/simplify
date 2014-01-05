# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'meal_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('yelp_url', self.gf('django.db.models.fields.URLField')(max_length=500)),
        ))
        db.send_create_signal(u'meal', ['Restaurant'])

        # Adding model 'RestaurantVisit'
        db.create_table(u'meal_restaurantvisit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meal.Restaurant'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'meal', ['RestaurantVisit'])

    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'meal_restaurant')

        # Deleting model 'RestaurantVisit'
        db.delete_table(u'meal_restaurantvisit')

    models = {
        u'meal.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'yelp_url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'meal.restaurantvisit': {
            'Meta': {'object_name': 'RestaurantVisit'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meal.Restaurant']"})
        }
    }

    complete_apps = ['meal']
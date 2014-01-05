# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pants'
        db.create_table(u'wardrobe_pants', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'wardrobe', ['Pants'])

        # Adding model 'Shirt'
        db.create_table(u'wardrobe_shirt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'wardrobe', ['Shirt'])

        # Adding model 'Shoes'
        db.create_table(u'wardrobe_shoes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'wardrobe', ['Shoes'])

        # Adding model 'OutFit'
        db.create_table(u'wardrobe_outfit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pants', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.Pants'])),
            ('shirt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.Shirt'])),
            ('shoes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.Shoes'])),
        ))
        db.send_create_signal(u'wardrobe', ['OutFit'])

        # Adding model 'OutfitWear'
        db.create_table(u'wardrobe_outfitwear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('outfit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.OutFit'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'wardrobe', ['OutfitWear'])

    def backwards(self, orm):
        # Deleting model 'Pants'
        db.delete_table(u'wardrobe_pants')

        # Deleting model 'Shirt'
        db.delete_table(u'wardrobe_shirt')

        # Deleting model 'Shoes'
        db.delete_table(u'wardrobe_shoes')

        # Deleting model 'OutFit'
        db.delete_table(u'wardrobe_outfit')

        # Deleting model 'OutfitWear'
        db.delete_table(u'wardrobe_outfitwear')

    models = {
        u'wardrobe.outfit': {
            'Meta': {'object_name': 'OutFit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pants': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Pants']"}),
            'shirt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Shirt']"}),
            'shoes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Shoes']"})
        },
        u'wardrobe.outfitwear': {
            'Meta': {'object_name': 'OutfitWear'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outfit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.OutFit']"})
        },
        u'wardrobe.pants': {
            'Meta': {'object_name': 'Pants'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wardrobe.shirt': {
            'Meta': {'object_name': 'Shirt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wardrobe.shoes': {
            'Meta': {'object_name': 'Shoes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wardrobe']
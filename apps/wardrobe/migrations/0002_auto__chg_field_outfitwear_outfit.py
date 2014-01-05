# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OutfitWear.outfit'
        db.alter_column(u'wardrobe_outfitwear', 'outfit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.Outfit']))
    def backwards(self, orm):

        # Changing field 'OutfitWear.outfit'
        db.alter_column(u'wardrobe_outfitwear', 'outfit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wardrobe.OutFit']))
    models = {
        u'wardrobe.outfit': {
            'Meta': {'object_name': 'Outfit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pants': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Pants']"}),
            'shirt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Shirt']"}),
            'shoes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Shoes']"})
        },
        u'wardrobe.outfitwear': {
            'Meta': {'object_name': 'OutfitWear'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outfit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wardrobe.Outfit']"})
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
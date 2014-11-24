# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Gallery.caption'
        db.alter_column(u'gallery_gallery', 'caption', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Gallery.caption'
        db.alter_column(u'gallery_gallery', 'caption', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

    models = {
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'caption': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 20, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 20, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'thumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
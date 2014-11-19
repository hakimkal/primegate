# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'gallery_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('thumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 19, 0, 0), auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 19, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'gallery', ['Gallery'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'gallery_gallery')


    models = {
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'thumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
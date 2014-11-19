# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Homepagebanner'
        db.create_table(u'homepagebanners_homepagebanner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('brief_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'homepagebanners', ['Homepagebanner'])


    def backwards(self, orm):
        # Deleting model 'Homepagebanner'
        db.delete_table(u'homepagebanners_homepagebanner')


    models = {
        u'homepagebanners.homepagebanner': {
            'Meta': {'object_name': 'Homepagebanner'},
            'brief_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['homepagebanners']
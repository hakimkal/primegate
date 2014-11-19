# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Homepagebanner.created'
        db.add_column(u'homepagebanners_homepagebanner', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 19, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Homepagebanner.modified'
        db.add_column(u'homepagebanners_homepagebanner', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 19, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Homepagebanner.created'
        db.delete_column(u'homepagebanners_homepagebanner', 'created')

        # Deleting field 'Homepagebanner.modified'
        db.delete_column(u'homepagebanners_homepagebanner', 'modified')


    models = {
        u'homepagebanners.homepagebanner': {
            'Meta': {'object_name': 'Homepagebanner'},
            'brief_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['homepagebanners']
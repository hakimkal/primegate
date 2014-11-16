# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Nlsubscriber', fields ['email']
        db.create_unique(u'nlsubscribers_nlsubscriber', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Nlsubscriber', fields ['email']
        db.delete_unique(u'nlsubscribers_nlsubscriber', ['email'])


    models = {
        u'nlsubscribers.nlsubscriber': {
            'Meta': {'object_name': 'Nlsubscriber'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nlsubscribers']
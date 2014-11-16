# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Nlsubscriber.created'
        db.add_column(u'nlsubscribers_nlsubscriber', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 16, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Nlsubscriber.modified'
        db.add_column(u'nlsubscribers_nlsubscriber', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 16, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Nlsubscriber.created'
        db.delete_column(u'nlsubscribers_nlsubscriber', 'created')

        # Deleting field 'Nlsubscriber.modified'
        db.delete_column(u'nlsubscribers_nlsubscriber', 'modified')


    models = {
        u'nlsubscribers.nlsubscriber': {
            'Meta': {'object_name': 'Nlsubscriber'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nlsubscribers']
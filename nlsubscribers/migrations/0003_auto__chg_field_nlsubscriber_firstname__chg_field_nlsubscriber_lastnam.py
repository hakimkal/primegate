# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Nlsubscriber.firstname'
        db.alter_column(u'nlsubscribers_nlsubscriber', 'firstname', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Nlsubscriber.lastname'
        db.alter_column(u'nlsubscribers_nlsubscriber', 'lastname', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

    def backwards(self, orm):

        # Changing field 'Nlsubscriber.firstname'
        db.alter_column(u'nlsubscribers_nlsubscriber', 'firstname', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Nlsubscriber.lastname'
        db.alter_column(u'nlsubscribers_nlsubscriber', 'lastname', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    models = {
        u'nlsubscribers.nlsubscriber': {
            'Meta': {'object_name': 'Nlsubscriber'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nlsubscribers']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nlsubscriber'
        db.create_table(u'nlsubscribers_nlsubscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
        ))
        db.send_create_signal(u'nlsubscribers', ['Nlsubscriber'])


    def backwards(self, orm):
        # Deleting model 'Nlsubscriber'
        db.delete_table(u'nlsubscribers_nlsubscriber')


    models = {
        u'nlsubscribers.nlsubscriber': {
            'Meta': {'object_name': 'Nlsubscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'})
        }
    }

    complete_apps = ['nlsubscribers']
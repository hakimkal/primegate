# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'team_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'team', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'team_team')


    models = {
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['team']
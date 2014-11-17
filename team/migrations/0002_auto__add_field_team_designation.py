# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Team.designation'
        db.add_column(u'team_team', 'designation',
                      self.gf('django.db.models.fields.CharField')(default='Staff', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Team.designation'
        db.delete_column(u'team_team', 'designation')


    models = {
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'default': "'Staff'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['team']
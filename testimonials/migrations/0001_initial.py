# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Testimonial'
        db.create_table(u'testimonials_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('remark', self.gf('django.db.models.fields.TextField')()),
            ('designation', self.gf('django.db.models.fields.CharField')(default='Parent', max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 18, 0, 0), auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'testimonials', ['Testimonial'])


    def backwards(self, orm):
        # Deleting model 'Testimonial'
        db.delete_table(u'testimonials_testimonial')


    models = {
        u'testimonials.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'default': "'Parent'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'remark': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['testimonials']
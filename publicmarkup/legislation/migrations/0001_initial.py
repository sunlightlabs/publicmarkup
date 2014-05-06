# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'legislation_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'legislation', ['Resource'])

        # Adding model 'Legislation'
        db.create_table(u'legislation_legislation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('allow_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'legislation', ['Legislation'])

        # Adding model 'Title'
        db.create_table(u'legislation_title', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legislation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='titles', to=orm['legislation.Legislation'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('extra_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'legislation', ['Title'])

        # Adding model 'Section'
        db.create_table(u'legislation_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sections', to=orm['legislation.Title'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'legislation', ['Section'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'legislation_resource')

        # Deleting model 'Legislation'
        db.delete_table(u'legislation_legislation')

        # Deleting model 'Title'
        db.delete_table(u'legislation_title')

        # Deleting model 'Section'
        db.delete_table(u'legislation_section')


    models = {
        u'legislation.legislation': {
            'Meta': {'object_name': 'Legislation'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'legislation.resource': {
            'Meta': {'object_name': 'Resource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'legislation.section': {
            'Meta': {'ordering': "['number', 'name']", 'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['legislation.Title']"})
        },
        u'legislation.title': {
            'Meta': {'ordering': "['number', 'name']", 'object_name': 'Title'},
            'extra_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'titles'", 'to': u"orm['legislation.Legislation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['legislation']
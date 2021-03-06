# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table(u'blogs_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owned_blogs', to=orm['users.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=20)),
            ('posts_per_page', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'blogs', ['Blog'])

        # Adding M2M table for field collaborators on 'Blog'
        m2m_table_name = db.shorten_name(u'blogs_blog_collaborators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm[u'blogs.blog'], null=False)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'user_id'])

        # Adding model 'Post'
        db.create_table(u'blogs_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('status', self.gf('model_utils.fields.StatusField')(default='published', max_length=100, no_check_for_status=True)),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status')),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['blogs.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authored_blog_posts', to=orm['users.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('raw_content', self.gf('django.db.models.fields.TextField')()),
            ('rendered_html', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'blogs', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table(u'blogs_blog')

        # Removing M2M table for field collaborators on 'Blog'
        db.delete_table(db.shorten_name(u'blogs_blog_collaborators'))

        # Deleting model 'Post'
        db.delete_table(u'blogs_post')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'authoring_blogs'", 'symmetrical': 'False', 'to': u"orm['users.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_blogs'", 'to': u"orm['users.User']"}),
            'posts_per_page': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '20'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blogs.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authored_blog_posts'", 'to': u"orm['users.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['blogs.Blog']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'raw_content': ('django.db.models.fields.TextField', [], {}),
            'rendered_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'published'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['blogs']
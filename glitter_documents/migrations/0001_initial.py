# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('published', models.BooleanField(db_index=True, default=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('document', models.FileField(max_length=200, upload_to='documents/document/%Y/%m')),
                ('author', models.CharField(blank=True, max_length=32)),
                ('file_size', models.PositiveIntegerField(editable=False, default=0)),
                ('summary', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='blanc_documents.Category')),
                ('current_version', models.ForeignKey(null=True, blank=True, editable=False, to='glitter.Version')),
            ],
            options={
                'get_latest_by': 'created_at',
                'ordering': ('-created_at',),
                'default_permissions': ('add', 'change', 'delete', 'edit', 'publish'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, db_index=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_format',
            field=models.ForeignKey(to='blanc_documents.Format'),
        ),
    ]

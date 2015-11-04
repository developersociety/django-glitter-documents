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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('document', models.FileField(max_length=200, upload_to=b'documents/document/%Y/%m')),
                ('file_size', models.PositiveIntegerField(default=0, editable=False)),
                ('summary', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='blanc_documents.Category')),
                ('current_version', models.ForeignKey(blank=True, editable=False, to='glitter.Version', null=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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

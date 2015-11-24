# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0002_owner_optional'),
        ('blanc_documents', '0002_document_indexes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestDocumentsBlock',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category', models.ForeignKey(to='blanc_documents.Category', null=True, blank=True)),
                ('content_block', models.ForeignKey(to='glitter.ContentBlock', editable=False, null=True)),
            ],
            options={
                'verbose_name': 'latest documents',
            },
        ),
    ]

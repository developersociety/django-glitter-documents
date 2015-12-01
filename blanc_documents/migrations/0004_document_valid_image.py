# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blanc_documents', '0003_latestdocumentsblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='valid_image',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]

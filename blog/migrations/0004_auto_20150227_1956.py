# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150227_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='publish',
            new_name='published',
        ),
    ]

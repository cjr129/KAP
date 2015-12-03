# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnightsAssistantPlanner', '0020_events_location'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='workouts',
            unique_together=set([('month', 'day', 'year', 'user')]),
        ),
    ]

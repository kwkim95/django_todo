# Generated by Django 3.2.5 on 2021-07-22 01:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 1, 53, 32, 32398, tzinfo=utc), verbose_name='date'),
        ),
    ]

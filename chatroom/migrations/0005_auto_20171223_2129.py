# Generated by Django 2.0 on 2017-12-23 21:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_auto_20171223_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2017, 12, 23, 21, 29, 33, 295148, tzinfo=utc)),
        ),
    ]

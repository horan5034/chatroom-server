# Generated by Django 2.0 on 2017-12-23 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0003_auto_20171223_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='message',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2017, 12, 23, 19, 18, 50, 759308, tzinfo=utc)),
        ),
    ]

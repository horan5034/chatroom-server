# Generated by Django 2.0 on 2017-12-23 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomsmessages',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='roomsmessages',
            name='rooms',
        ),
        migrations.DeleteModel(
            name='RoomsMessages',
        ),
    ]

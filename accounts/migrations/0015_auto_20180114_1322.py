# Generated by Django 2.0 on 2018-01-14 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180113_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='private_messages_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='private_messages_limit',
        ),
    ]

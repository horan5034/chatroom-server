# Generated by Django 2.0 on 2018-02-04 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0016_auto_20180204_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversations',
            name='host',
        ),
        migrations.RemoveField(
            model_name='conversations',
            name='invitee',
        ),
        migrations.DeleteModel(
            name='Conversations',
        ),
    ]
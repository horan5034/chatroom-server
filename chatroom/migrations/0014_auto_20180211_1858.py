# Generated by Django 2.0 on 2018-02-11 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0013_auto_20180129_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrooms',
            old_name='host_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userrooms',
            name='invitee_id',
        ),
    ]
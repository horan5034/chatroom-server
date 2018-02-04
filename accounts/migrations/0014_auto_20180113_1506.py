# Generated by Django 2.0 on 2018-01-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_user_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='private_messages_joined',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='private_messages_limit',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='rooms_joined',
            field=models.IntegerField(),
        ),
    ]

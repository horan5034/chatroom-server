# Generated by Django 2.0 on 2018-01-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_room_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rooms_joined',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='room_limit',
            field=models.IntegerField(default=10),
        ),
    ]

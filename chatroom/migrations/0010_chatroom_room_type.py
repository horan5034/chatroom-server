# Generated by Django 2.0 on 2018-01-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0009_auto_20171226_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='room_type',
            field=models.CharField(default='public', max_length=10),
        ),
    ]

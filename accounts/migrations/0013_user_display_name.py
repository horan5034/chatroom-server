# Generated by Django 2.0 on 2018-01-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180104_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(default='Change Me', max_length=15),
        ),
    ]

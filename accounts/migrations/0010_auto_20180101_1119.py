# Generated by Django 2.0 on 2018-01-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_profile_picture_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture_path',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
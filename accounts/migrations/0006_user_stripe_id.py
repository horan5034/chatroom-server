# Generated by Django 2.0 on 2017-12-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_user_subscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]

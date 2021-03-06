# Generated by Django 2.0 on 2017-12-24 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubscriptions',
            name='Subscription',
        ),
        migrations.RemoveField(
            model_name='usersubscriptions',
            name='user',
        ),
        migrations.AddField(
            model_name='subscription',
            name='user_subscription_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserSubscriptions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_subscription_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserSubscriptions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubscriptions',
            name='Subscriptions',
            field=models.IntegerField(default=1982),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubscriptions',
            name='users',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

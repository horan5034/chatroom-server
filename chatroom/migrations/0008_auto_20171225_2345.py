# Generated by Django 2.0 on 2017-12-25 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0007_auto_20171224_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mesages', to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=10)
    cost = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)

    is_subscribed = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    subscriptions = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING, null=True)
    
    profile_picture_path = models.CharField(max_length=1000, null=True)
    
    room_limit = models.IntegerField(null=False, default=10)
    rooms_joined = models.IntegerField(null=False, default=1)
    
    display_name = models.CharField(null=False, max_length=15, default="Change Me")
    objects = AccountUserManager()

    socket_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email


 
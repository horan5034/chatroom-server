from django.db import models
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.conf import settings

# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=20, null=False)
    tag = models.CharField(max_length=20, null=True)
    room_type = models.CharField(max_length=10, null=False, default="public")


class UserRooms(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.DO_NOTHING, null=False)
=======
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.DO_NOTHING, null=False)
    invitee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
    room = models.ForeignKey(Chatroom, on_delete=models.DO_NOTHING)


class Message(models.Model):
    message = models.CharField(max_length=500, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Chatroom, on_delete=models.DO_NOTHING, null=True)

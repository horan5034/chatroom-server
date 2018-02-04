from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Chatroom, Message, UserRooms
from accounts.serializers import UserSerializer

class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageReaderSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class UserRoomSerializer(serializers.ModelSerializer):
    room_id = serializers.StringRelatedField(many=False)
    user_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserRooms
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
     class Meta:
        model = Token
        fields = ('key', 'user')

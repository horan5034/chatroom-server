from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User, Subscription


class RegisterUserSerializer(RegisterSerializer):
    display_name = serializers.CharField(required=True, write_only=True)
    
    def custom_signup(self, request, user):
        user.display_name = self.validated_data.get('display_name')
        user.save(update_fields=['display_name'])



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

     
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_auth.registration.views import RegisterView
from .models import User, Subscription
from chatroom.models import UserRooms
from .serializers import UserSerializer, SubscriptionSerializer, RegisterUserSerializer
from django.conf import settings
import stripe
import datetime

from django.contrib import messages, auth

# Create your views here.
class UserView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            users = User.objects.all()
<<<<<<< HEAD
            if users is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

=======
>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
            serializer = UserSerializer(users, many=True)

            if users is None and not serializer.is_valid():
                return Response(status=status.HTTP_404_NOT_FOUND)

            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
<<<<<<< HEAD
            user = User.objects.get(id=pk)
            if User is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user)
            serialized_data = serializer.data

            return Response(serialized_data,
                            status=status.HTTP_200_OK)

=======
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)

            if user is None and not serializer.is_valid():
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)
>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
    
    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if user is None and not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data)


    def put(self, request):
        user = request.data['user']

        stripe.api_key=settings.STRIPE_SECRET
        customer = stripe.Customer.create(
                    email=user['email'],
                    card=request.data['stripe_token'],
                    plan='STANDARD_CHAT',
                )

        if customer:
            serializer = UserSerializer(user, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)

    def post(self, request, pk = None):
        user = User.objects.get(id=pk)
<<<<<<< HEAD
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
=======

        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
        stripe.api_key=settings.STRIPE_SECRET
        customer = stripe.Customer.retrieve(user.stripe_id)
        customer.cancel_subscription(at_period_end=True)

        user.is_subscibed = False
        user.save()

        return Response(status=status.HTTP_200_OK)

class SubscriptionView(APIView):
    def get(selfself, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)


class NameRegistrationView(RegisterView):
    serializer_class = RegisterUserSerializer

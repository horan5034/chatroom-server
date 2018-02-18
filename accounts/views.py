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

            if users is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(users, many=True)

            if users is None and not serializer.is_valid():
                return Response(status=status.HTTP_404_NOT_FOUND)

            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=pk)
            if User is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user)
            serialized_data = serializer.data

            return Response(serialized_data,
                            status=status.HTTP_200_OK)

    
    def patch(self, request, pk):
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        user_data = request.data['user']
        user = User.objects.get(email=user_data['email'])

        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stripe.api_key = settings.STRIPE_SECRET
        customer = stripe.Charge.create(
                    amount=1000,
                    currency="GBP",
                    description="Chatrooms Standard Payment",
                    card=request.data['stripe_token'],
                )

        if customer.paid:
            user.is_subscribed = True
            user.stripe_id = customer['id']

            user.save()

            serializer = UserSerializer(user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk=None):
        user = User.objects.get(id=pk)

        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        stripe.api_key = settings.STRIPE_SECRET
        customer = stripe.Customer.retrieve(user.stripe_id)

        if customer is not None:
            customer.cancel_subscription(at_period_end=True)

            user.is_subscribed = False
            user.save()

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class SubscriptionView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)


class NameRegistrationView(RegisterView):
    serializer_class = RegisterUserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Subscription
from chatroom.models import UserRooms
from .serializers import UserSerializer, SubscriptionSerializer
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
            serialized_data = serializer.data
                
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=pk)
            if user is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserSerializer(user, many=False)
            serialized_data = serializer.data
            
            return Response(serialized_data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
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
   

class SubscriptionView(APIView):
    def get(selfself, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)

    
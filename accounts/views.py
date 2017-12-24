from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import User, Subscription
from .serializers import UserSerializer, SubscriptionSerializer

from django.contrib import messages, auth

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and retrieving users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # @detail_route(methods=['GET'], url_path='login')
    # def login(self, request):
    #
    #     user = auth.authenticate(email=request.POST.get('email'),
    #                              password=request.POST.get('password'))
    #     serialized_data = UserSerializer(user, many=False)
    #
    #     if user is not None:
    #         auth.login(request, user)
    #
    #         return Response(serialized_data.data,
    #                         status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
    

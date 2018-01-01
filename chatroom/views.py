from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import ChatroomSerializer, MessageSerializer, MessageReaderSerializer, UserRoomSerializer
from .models import Chatroom, Message, UserRooms
from accounts.models import User


# Create your views here.
class ChatroomView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            rooms = Chatroom.objects.all()
            serializer = ChatroomSerializer(rooms, many=True)
            serialized_data = serializer.data
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            room = Chatroom.objects.get(id=pk)
            serializer = ChatroomSerializer(room, many=False)
            serialized_data = serializer.data
        
            return Response(serialized_data, status=status.HTTP_200_OK)


    @detail_route()
    def get_messages(self, request, pk=None):
        room = self.get_object()

        if room is not None:
            messages = Message.objects.filter(room_id=room.id)
            serialized_data = MessageReaderSerializer(messages, many=True)

            return Response(serialized_data.data, 
                            status=status.HTTP_200_OK) 
        else: 
            return Response(status=status.HTTP_404_NOT_FOUND)


class MessageView(APIView):
    def get(self, request, pk=None):
        try:
            limit = int(request.query_params['limit'])
            offset = int(request.query_params['offset'])        
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            messages = Message.objects.filter(room_id=pk)\
                .order_by('-id')[offset:offset+limit]
            serializer = MessageReaderSerializer(messages, many=True)
            serialized_data = serializer.data
            
            return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserRoomView(APIView):
    
    def get(self, request, pk=None):
        user_room_ids = UserRooms.objects.filter(user_id=pk).values_list('room_id', flat=True)
        if user_room_ids is None: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        rooms = Chatroom.objects.filter(id__in=user_room_ids)
        if rooms is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ChatroomSerializer(rooms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRoomSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)


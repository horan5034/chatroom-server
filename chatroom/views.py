from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import ChatroomSerializer, MessageSerializer, MessageReaderSerializer, UserRoomSerializer
from .models import Chatroom, Message, UserRooms
from accounts.models import User


# Create your views here.
class ChatroomViewSet(viewsets.ModelViewSet):
    serializer_class = ChatroomSerializer
    queryset = Chatroom.objects.all()

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


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class MessageReaderViewset(viewsets.ModelViewSet):
    serializer_class = MessageReaderSerializer
    queryset = Message.objects.all()

class UserRoomViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoomSerializer
    queryset = UserRooms.objects.all()

    @detail_route(url_path='get_rooms')
    def get_room_by_user_id(self, request, pk=None):
        user_room_ids = UserRooms.objects.filter(user_id=pk).values_list('room_id', flat=True)
        room_ids = Chatroom.objects.filter(id__in=user_room_ids)
        rooms = Chatroom.objects.filter(id__in=room_ids)

        if rooms is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_data = ChatroomSerializer(rooms, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

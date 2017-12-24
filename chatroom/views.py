from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .serializers import ChatroomSerializer, MessageSerializer, UserRoomSerializer
from .models import Chatroom, Message, UserRooms


# Create your views here.
class ChatroomViewSet(viewsets.ModelViewSet):
    serializer_class = ChatroomSerializer
    queryset = Chatroom.objects.all()

    @detail_route()
    def get_messages(self, request, pk=None):
        room = self.get_object()

        if room is not None:
            messages = Message.objects.filter(room_id=room.id)
            serialized_data = MessageSerializer(messages, many=True)

            return Response(serialized_data.data, 
                            status=status.HTTP_200_OK) 
        else: 
            return Response(status=status.HTTP_404_NOT_FOUND)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class UserRoomViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoomSerializer
    queryset = UserRooms.objects.all()

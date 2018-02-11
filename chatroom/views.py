from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatroomSerializer, MessageSerializer, MessageReaderSerializer, \
    UserRoomSerializer
from .models import Chatroom, Message, UserRooms
from accounts.models import User


# Create your views here.
class ChatroomView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            if request.query_params is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            search_term = request.query_params['searchTerm']
            user_id = request.query_params['userId']

            searchable_rooms = Chatroom.objects.filter(Q(name__icontains=search_term) |
                                                       Q(tag__icontains=search_term))

            filtered_rooms = UserRooms.objects.filter(room_id__in=searchable_rooms) \
                .exclude(user_id=user_id) \
                .distinct() \
                .values_list('room_id', flat=True)

            results = Chatroom.objects.filter(id__in=filtered_rooms)

            serializer = ChatroomSerializer(results, many=True)
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            room = Chatroom.objects.get(id=pk)
            serializer = ChatroomSerializer(room, many=False)
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
            new_room = Chatroom.objects.create(room_type=request.data['type'], tag=request.data['tag'],
                                               name=request.data['name'])

            UserRooms.objects.create(room_id=new_room.id, user_id=request.data['user_id'])

            user = User.objects.get(pk=request.data['user_id'])
            user.rooms_joined += 1
            user.save()

            return Response(new_room,
                            status=status.HTTP_201_CREATED)
        

class MessageView(APIView):
    # get_room_messages
    def get(self, request, pk=None):
        try:
            limit = int(request.query_params['limit'])
            offset = int(request.query_params['offset'])
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            messages = Message.objects.filter(room_id=pk) \
                           .order_by('-id')[offset:offset + limit]
            serializer = MessageReaderSerializer(messages, many=True)
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_200_OK)

    # write_message
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
        if pk is not None:
            user_room_ids = UserRooms.objects.filter(user=pk).values_list('room_id', flat=True)

            if user_room_ids is None:
                return Response(status=status.HTTP_200_OK)

            rooms = Chatroom.objects.filter(id__in=user_room_ids)
            if rooms is None:
                return Response(status=status.HTTP_200_OK)

            serializer = ChatroomSerializer(rooms, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # add_to_room
    def post(self, request):
        serializer = UserRoomSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(pk=request.data['user'])
        user.rooms_joined += 1
        user.save()

        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

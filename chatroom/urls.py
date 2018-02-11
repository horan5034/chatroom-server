from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ChatroomView, MessageView, UserRoomView

urlpatterns = [
<<<<<<< HEAD
    url(r'get_rooms/(?P<pk>[0-9]+)/$', ChatroomView.as_view()),
    url(r'get_rooms/', ChatroomView.as_view()),
    url(r'get_room/(?P<pk>[0-9]+)/$', ChatroomView.as_view()),
    url(r'add_room/$', ChatroomView.as_view()),
    url(r'get_user_rooms/(?P<pk>[0-9]+)/$', UserRoomView.as_view()),
    url(r'add_to_room/$', UserRoomView.as_view()),
    url(r'get_room_messages/(?P<pk>[0-9]+)/$', MessageView.as_view()),
    url(r'write_message/', MessageView.as_view()),

=======
    url(r'chatrooms/(?P<pk>[0-9]+)/$', ChatroomView.as_view()),
    url(r'user_rooms/(?P<pk>[0-9]+)/$', UserRoomView.as_view()),
    url(r'messages/(?P<pk>[0-9]+)/$', MessageView.as_view()),
>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
]

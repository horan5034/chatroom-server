from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ChatroomView, MessageView, UserRoomView

urlpatterns = [
    url(r'chatrooms/(?P<pk>[0-9]+)/$', ChatroomView.as_view()),
    url(r'user_rooms/(?P<pk>[0-9]+)/$', UserRoomView.as_view()),
    url(r'messages/(?P<pk>[0-9]+)/$', MessageView.as_view()),
]

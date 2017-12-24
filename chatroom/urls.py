from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ChatroomViewSet, MessageViewSet, UserRoomViewSet
from config.settings import API_VERSION

router = DefaultRouter()
router.register(prefix=API_VERSION+'messages', viewset=MessageViewSet)
router.register(prefix=API_VERSION+'chatroom', viewset=ChatroomViewSet)
router.register(prefix=API_VERSION+'user_rooms', viewset=UserRoomViewSet)

urlpatterns = router.urls

# url(r''+API_VERSION + 'chatroom/(?P<pk>[0-9]+)/$', ChatroomView.as_view()),
# url(r''+API_VERSION+'messages/(?P<room_id>[0-9]+)/$', MessageView.as_view()),
    
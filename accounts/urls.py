from accounts.views import UserView, SubscriptionView
from config.settings import API_VERSION
from django.conf.urls import url

urlpatterns = [
<<<<<<< HEAD
    url(r'(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'update/(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'subscribe/$', UserView.as_view()),
=======
    url(r'users/$', UserView.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', UserView.as_view()),
>>>>>>> 22ff81903a810015e642b05b5a54a0fadd16e6b2
    url(r'cancel_subscription/(?P<pk>[0-9]+)/$', UserView.as_view()),

]

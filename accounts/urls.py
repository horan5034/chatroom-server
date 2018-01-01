from accounts.views import UserView, SubscriptionView
from config.settings import API_VERSION
from django.conf.urls import url

urlpatterns = [
    url(r'users/$', UserView.as_view()),
    url(r'user/(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'update/(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'subscription/$', UserView.as_view()),

]

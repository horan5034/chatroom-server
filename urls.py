from config.settings import API_VERSION
from django.conf.urls import url, include
from django.contrib import admin

# router = DefaultRouter()
# router.register(prefix=API_VERSION+'accounts', viewset=UserViewSet)
# router.register(prefix=API_VERSION+'accounts_reader', viewset=UserReaderViewSet)
# router.register(prefix=API_VERSION+'subscriptions', viewset=SubscriptionViewSet)

urlpatterns = [
    url(r'^'+API_VERSION+'admin/', admin.site.urls),
    url(r'^'+API_VERSION+'rooms/', include('chatroom.urls')),
    url(r'^'+API_VERSION+'users/', include('accounts.urls')),
    url(r'^'+API_VERSION+'rest-auth/', include('rest_auth.urls')),
    url(r'^'+API_VERSION+'rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include('django.contrib.auth.urls')),

]

# urlpatterns += router.urls
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, SubscriptionViewSet
from config.settings import API_VERSION

router = DefaultRouter()
router.register(prefix=API_VERSION+'user', viewset=UserViewSet)
router.register(prefix=API_VERSION+'subscription', viewset=SubscriptionViewSet)

urlpatterns = router.urls

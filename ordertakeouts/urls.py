from django.conf.urls import url, include
from .views import LocationsViewSet, OrdersViewSet, UsersViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter(trailing_slash=False)

router.register(r'locations', LocationsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = router.urls

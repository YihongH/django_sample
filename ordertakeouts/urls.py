from django.conf.urls import url, include
from .views.locations import LocationList, LocationDetail
from .views.orders import OrderList, OrderDetail
from .views.users import UserList, UserDetail
# from rest_framework.routers import DefaultRouter



# router = DefaultRouter(trailing_slash=False)

# router.register(r'locations', LocationsViewSet)
# router.register(r'orders', OrdersViewSet)
# router.register(r'users', UsersViewSet)

# urlpatterns = router.urls


urlpatterns = [
    url(r'^locations/$', LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', LocationDetail.as_view()),
    url(r'^locations/(?P<location_id>[0-9]+)/orders$', OrderList.as_view()),
    # url(r'^locations/(?P<location_id>[0-9]+)/orders?created_time=(?P<year>[0-9]{4})(?P<month>[0-9]{2})(?P<day>[0-9]{2})/$', OrderList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)$', OrderDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view()),


]
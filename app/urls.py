from django.conf.urls import url, include
from .views import *

 # CreateUserView
# from rest_framework.routers import DefaultRouter



# router = DefaultRouter(trailing_slash=False)

# router.register(r'locations', LocationsViewSet)
# router.register(r'orders', OrdersViewSet)
# router.register(r'users', UsersViewSet)

# urlpatterns = router.urls


urlpatterns = [
    url(r'^location/$', LocationList.as_view()),
    url(r'^location/(?P<pk>[0-9]+)$', LocationDetail.as_view()),
    url(r'^location/(?P<location_id>[0-9]+)/order$', OrderList.as_view()),
    # url(r'^locations/(?P<location_id>[0-9]+)/orders?created_time=(?P<year>[0-9]{4})(?P<month>[0-9]{2})(?P<day>[0-9]{2})/$', OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)$', OrderDetail.as_view()),
    url(r'^user/$', UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view()),

    # url(r'^users/register$', CreateUserView.as_view()),

]
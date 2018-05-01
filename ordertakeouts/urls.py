from django.conf.urls import url, include
from .views import LocationList, LocationDetail, OrderList, OrderDetail, UserList, UserDetail
# from rest_framework.routers import DefaultRouter



# router = DefaultRouter(trailing_slash=False)

# router.register(r'locations', LocationsViewSet)
# router.register(r'orders', OrdersViewSet)
# router.register(r'users', UsersViewSet)

# urlpatterns = router.urls


urlpatterns = [
    url(r'^locations/$', LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', LocationDetail.as_view()),
    url(r'^locations/(?P<location_id>[0-9]+)/orders/$', OrderList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)$', OrderDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view()),

]
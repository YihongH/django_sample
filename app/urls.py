from django.conf.urls import url, include
# from django.contrib.auth.decorators import login_required
from .views import *
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

# router = DefaultRouter(trailing_slash=False)

# router.register(r'locations', LocationsViewSet)
# router.register(r'orders', OrdersViewSet)
# router.register(r'users', UsersViewSet)

# urlpatterns = router.urls
# router = routers.DefaultRouter()
# router.register(r'accounts', UserView, 'list')


urlpatterns = [
   
    url(r'^location$', LocationList.as_view(), name='location-list'),
    url(r'^location/(?P<pk>[0-9]+)$', LocationDetail.as_view(), name='location-detail'),
    
    url(r'^location/(?P<location_id>[0-9]+)/order$', OrderList.as_view(), name='order-list'),
    url(r'^location/(?P<location_id>[0-9]+)/order?created_time=(?P<year>[0-9]{4})(?P<month>[0-9]{2})(?P<day>[0-9]{2})/$', OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)$', OrderDetail.as_view(), name='order-detail'),

  
    url(r'^user$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),

    
    url(r'^user/register$', CreateUserView.as_view(), name='user-create'),
    url(r'^user/token$', obtain_jwt_token),
    url(r'^user/token/refresh$', refresh_jwt_token),
    url(r'^user/token/verify$', verify_jwt_token),
    # url(r'', include(router.urls)),
]


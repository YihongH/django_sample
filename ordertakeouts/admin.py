from django.contrib import admin
from ordertakeouts.models.locations import Locations
from ordertakeouts.models.orders import Orders
from ordertakeouts.models.users import Users


admin.site.register(Locations)
admin.site.register(Orders)
admin.site.register(Users)
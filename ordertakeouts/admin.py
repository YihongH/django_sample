from django.contrib import admin
from ordertakeouts.models.model_locations import Locations
from ordertakeouts.models.model_orders import Orders
from ordertakeouts.models.model_users import Users


admin.site.register(Locations)
admin.site.register(Orders)
admin.site.register(Users)
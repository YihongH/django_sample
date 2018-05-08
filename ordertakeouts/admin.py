from django.contrib import admin
from ordertakeouts.models.location import Location
from ordertakeouts.models.order import Order
from ordertakeouts.models.user import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User


# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class UsersInline(admin.StackedInline):
#     model = Users
#     can_delete = False
#     verbose_name_plural = 'users'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UsersInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Location)
admin.site.register(Order)
admin.site.register(User)
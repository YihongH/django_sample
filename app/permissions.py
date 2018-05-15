from rolepermissions.permissions import register_object_checker
from app.roles import SystemAdmin, Delivery


@register_object_checker()
def access_order(role, user, order):
    if role == SystemAdmin:
        return True

    if role == Delevery:
        return True

    if order.user == user:
        return True

    return False


# def update_order(role, user, order):
#     if role == SystemAdmin:
#         return True

#     if role == Delevery:
#         return True

#     if order.user == user:
#         return True

#     return False
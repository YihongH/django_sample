from rolepermissions.roles import AbstractUserRole


class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'create_order': True,
        'read_order': True,
        'update_order': True,
        'delet_order': True,
    }

class Delivery(AbstractUserRole):
    available_permissions = {
        'read_order': True,
        'update_order': True,
        'delet_order': True
    }

class Customer(AbstractUserRole):
    available_permissions = {
        'read_order': True,
        'create_order': True,
        'update_order': True,
    }
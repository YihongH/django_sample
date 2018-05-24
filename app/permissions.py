from rest_framework import permissions

class OrderPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return request.user.has_perm('app.view_order')        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_order')
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_order')
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_order')
        return False

    def has_object_permission(self, request, view, obj):         
        if request.method in ['GET']:
            return request.user.has_perm('app.view_order', obj)        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_order', obj)
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_order', obj)
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_order', obj)
        return False


class UserPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return request.user.has_perm('app.view_user')        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_user')
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_user')
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_user')
        return False

    def has_object_permission(self, request, view, obj):         
        if request.method in ['GET']:
            return request.user.has_perm('app.view_user', obj)        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_user', obj)
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_user', obj)
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_user', obj)
        return False

class LocationPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return request.user.has_perm('app.view_location')        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_location')
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_location')
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_location')
        return False

    def has_object_permission(self, request, view, obj):         
        if request.method in ['GET']:
            return request.user.has_perm('app.view_location', obj)        
        if request.method in ['POST']:
            return request.user.has_perm('app.add_location', obj)
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('app.change_location', obj)
        if request.method in ['DELETE']:
            return request.user.has_perm('app.delete_location', obj)
        return False
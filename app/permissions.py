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



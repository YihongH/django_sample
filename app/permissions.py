from rest_framework import permissions


class OrderPermissions(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        options = {'GET': request.user.has_perm('app.view_order'), 
           'POST': request.user.has_perm('app.add_order'), 
           'PUT': request.user.has_perm('app.change_order'), 
           'PATCH': request.user.has_perm('app.change_order'), 
           'DELETE': request.user.has_perm('app.delete_order')}
        return options.get(request.method, False)

    # def has_permission(self, request, view):
    #     if request.method in ['GET']:
    #         return request.user.has_perm('app.view_order')        
    #     if request.method in ['POST']:
    #         return request.user.has_perm('app.add_order')
    #     if request.method in ['PUT', 'PATCH']:
    #         return request.user.has_perm('app.change_order')
    #     if request.method in ['DELETE']:
    #         return request.user.has_perm('app.delete_order')
    #     return False

    def has_object_permission(self, request, view, obj):
        options_for_object = {'GET': request.user.has_perm('app.view_order', obj), 
           'POST': request.user.has_perm('app.add_order', obj), 
           'PUT': request.user.has_perm('app.change_order', obj), 
           'PATCH': request.user.has_perm('app.change_order', obj), 
           'DELETE': request.user.has_perm('app.delete_order', obj)}
        return options_for_object.get(request.method, False)

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class CustomModelPermissions(permissions.DjangoModelPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }



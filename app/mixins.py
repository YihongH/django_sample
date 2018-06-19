from django.contrib.auth.models import Group
from app.models import GroupProfile

# Default settings
DEFAULT_GROUPS = ('admin', 'delivery', 'customer')
DEFAULT_REGISTRY = (
    "get_queryset",
    "get_serializer_class",
    "perform_create",
    "perform_update",
    "perform_destroy",
)

class RoleError(Exception):
    """Base class for exceptions in this module."""
    pass


class RoleViewSetMixin(object):
    """A ViewSet mixin that parameterizes DRF methods over roles"""
    # _viewset_method_registry = set(getattr(settings, "VIEWSET_METHOD_REGISTRY", DEFAULT_REGISTRY))
    _viewset_method_registry = set(DEFAULT_REGISTRY)
    _role_groups = set(DEFAULT_GROUPS)
    def _call_role_fn(self, fn, *args, **kwargs):
        """Attempts to call a role-scoped method"""
        try:
            # import pdb; pdb.set_trace()
            role_name = self._get_role(self.request.user)
            role_fn = "{}_for_{}".format(fn, role_name)
            return getattr(self, role_fn)(*args, **kwargs)
        except (AttributeError, RoleError):
            return getattr(super(RoleViewSetMixin, self), fn)(*args, **kwargs)

    def _get_role(self, user):
        """Retrieves the given user's role"""
        user_groups = set([group.name.lower() for group in user.groups.all()])
        user_role = self._role_groups.intersection(user_groups)
        
        if len(user_role) < 1:
            raise RoleError("The user is not a member of any role groups")
        elif len(user_role) > 1:
            user_level = min(GroupProfile.objects.get(group=group).level for group in user.groups.all())
            return GroupProfile.objects.get(level=user_level).group.name
        else:
            return user_role.pop()

def register_fn(fn):
    """Dynamically adds fn to RoleViewSetMixin"""
    def inner(self, *args, **kwargs):
        return self._call_role_fn(fn, *args, **kwargs)
    setattr(RoleViewSetMixin, fn, inner)


for fn in RoleViewSetMixin._viewset_method_registry:
    register_fn(fn)

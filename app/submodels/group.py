# from django.contrib.auth.models import Group, User
from django.db import models



class GroupProfile(models.Model):
    group = models.OneToOneField('auth.Group',on_delete=True, unique=True)
    level = models.PositiveIntegerField(unique=True, null=True)

    class Meta:
        db_table = 'groupProfile'

    def __str__(self):
        return self.group.name

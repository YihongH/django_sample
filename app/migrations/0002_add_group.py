# Generated by Django 2.0.5 on 2018-06-01 12:55

from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.management import create_permissions
from django.contrib.contenttypes.models import ContentType

def add_group_permissions(apps, schema_editor):

# Permissions are created in a post_migrate signal. 
# They don't exist the first time migrations are run after a new model is added. 
# It is probably easiest to run the post_migrate signal handler manually
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    def group_permissions(group_name, permissions):
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            for perm in permissions:
                add_perm = Permission.objects.get(codename=perm)
                group.permissions.add(add_perm)
            group.save()
    
    
    perms_admin = ['view_order', 'delete_order', 'add_order', 'change_order', 'add_location', 'change_location', 'delete_location', 'view_location', 'view_user', 'change_user', 'delete_user']
    group_permissions('admin', perms_admin)
    
    perms_delivery = ['view_order', 'change_order', 'view_location', 'view_user']
    group_permissions('delivery', perms_delivery)
    
    perms_customer = ['view_order', 'add_order', 'change_order', 'view_location']
    group_permissions('customer', perms_customer)

class Migration(migrations.Migration):
    # initial = True
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
    ]
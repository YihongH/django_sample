# Generated by Django 2.0.6 on 2018-06-19 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE auth_group ADD COLUMN level smallint NOT NULL;')
    ]

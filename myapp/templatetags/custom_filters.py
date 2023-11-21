# custom_filters.py
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_admin_permissions')
def has_admin_permissions(user):
    return user.is_authenticated and user.groups.filter(name='Administradores').exists()
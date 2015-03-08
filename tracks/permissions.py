from rest_framework import permissions
from models import AllowedIPs


class TracksPermission(permissions.BasePermission):
    """
    Custom permission to be used with tracks data
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        allowed_ip = AllowedIPs.objects.filter(ip_addr=ip_addr).exists()
        allowed_group = 'data_access_group' in [group.name for group in request.user.groups.all()]
        return allowed_ip and allowed_group
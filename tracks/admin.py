from django.contrib import admin
from tracks.models import *


class DataPointAdmin(admin.ModelAdmin):
    list_display = ('user_UUID', 'user_code', 'type', 'last_modified', 'created',)
    readonly_fields = ('user_UUID', 'user_code', 'type', 'encrypted_data', 'last_modified', 'created',)
    fields = ('user_UUID', 'user_code', 'type', 'encrypted_data', 'last_modified', 'created',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(DataPoint, DataPointAdmin)
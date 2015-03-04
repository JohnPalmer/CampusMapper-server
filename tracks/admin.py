from django.contrib import admin
from tracks.models import *


class DataPointAdmin(admin.ModelAdmin):
    list_display = ('user_UUID', 'user_code', 'type', 'last_modified', 'created',)


admin.site.register(DataPoint, DataPointAdmin)
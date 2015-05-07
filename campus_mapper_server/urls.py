from django.conf.urls import patterns, include, url
from django.contrib import admin
from tracks.views import show_user_code, download_fix_stats, download_reg_stats


urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('tracks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mobility_mapper_code/', show_user_code, name='show_user_code'),
    url(r'^fix_stats/', download_fix_stats, name='download_fix_stats'),
    url(r'^reg_stats/', download_reg_stats, name='download_reg_stats'),
    url(r'^$', show_user_code),
)


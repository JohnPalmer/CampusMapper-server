from django.conf.urls import patterns, include, url
from django.contrib import admin
from tracks.views import show_user_code


urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('tracks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mobility_mapper_code/', show_user_code, name='show_user_code'),
    url(r'^$', show_user_code),
)


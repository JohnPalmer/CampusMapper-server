from django.conf.urls import patterns, url, include
from rest_framework import routers
from tracks import views


router = routers.DefaultRouter()
router.register(r'data_points', views.DataPointViewSet)


urlpatterns = patterns('tracks.views',
    url(r'^', include(router.urls)),
)
from namespaces import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('gms.namespaces.views',
    url(r'^(?P<pk>[0-9]+)$', views.main, name="home"),
)

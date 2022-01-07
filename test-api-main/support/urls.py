from support import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.support.views',
    url(r'^$', views.support, name="support"),
    url(r'^docs/', views.docs, name='docs'),
)
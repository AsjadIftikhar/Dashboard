from django.urls.conf import path
from tenant import views
from django.conf import settings
from django.conf.urls import include

urlpatterns = [path('get-tenants/', views.get_tenants, name='get_tenants'),
               path('login/', views.login, name='login'),
               path('', views.home, name='login')
               ]

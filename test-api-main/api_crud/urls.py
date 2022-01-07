
from django.contrib import admin
from django.urls import include, path
from api_crud import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from gms import views
from hci.views import TaskViewSet, JobViewSet, InstanceViewSet, JobStatus, AllJobStatus, SystemTask, SystemTaskByID, JobTypes, queryEndPoint
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



router = DefaultRouter()

#********************************
router.register('tasks', TaskViewSet, basename='tasks')
router.register('jobs', JobViewSet, basename='jobs')
router.register('Instances', InstanceViewSet, basename='Instances')

#********************************

# router.register('namespace', NameSpaces, basename='namespace')

# schema_view = get_schema_view(
#     openapi.Info(
#         title="GMS API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="Test License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
# urls
urlpatterns = [

    # path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("home/", include("apps.home.urls")),             # UI Kits Html files

    path('get_regions/',views.GetRegions.as_view({'get':'list'}), name="get_regions"),
    path('get_tenants/',views.GetTenants.as_view({'get': 'list'}),name="get_tenants"),
    path('get_namespaces/',views.GetNamespaces.as_view({'get': 'list'}),name="get_namespaces"),

    path('create_namespace/',views.CreateNamespace.as_view(), name="create_namespace"),
    path('create_tenants/',views.CreateTenants.as_view(), name="create_tenants"),
    path('create_regions/',views.CreateRegions.as_view(), name="create_regions"),
# GetRegions
    
    # path('namespace/', include(router.urls)),
    # # path('api/v1/movies/', include('movies.urls')),
    # path('api/v1/auth/', include('authentication.urls')),


    # path('tenant/', include('tenant.urls')),


    path('admin/', admin.site.urls),

    # path('swagger/', schema_view.with_ui('swagger',
    #                                      cache_timeout=0), name='schema-swagger-ui'),

    # path('', schema_view.with_ui('swagger',
    #                                      cache_timeout=0), name='schema-swagger-ui'),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="schema-swagger-ui",
    ),

    # path('redoc/', schema_view.with_ui('redoc',
    #                                    cache_timeout=0), name='schema-redoc'),

    path('apiViewSet/', include(router.urls)),
    path('jobStatus/<int:id>/', JobStatus.as_view()),
    path('AllJobStatus/', AllJobStatus.as_view()),
    path('SystemTask/', SystemTask.as_view()),
    path('SystemTaskByID/<int:id>/', SystemTaskByID.as_view()),
    path('JobTypes/', JobTypes.as_view()),
    path('HCISearch/<str:token>/', queryEndPoint.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('auth_u.urls', 'auth_u'))),
    path('reports/', include(('reports.urls', 'reports'))),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
]

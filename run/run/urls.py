from django.contrib import admin
from django.urls import include, path

from . import views

schema_view = views.schema_view(
    title='Users API',
    description='API for users',
    version='1.0'
)


urlpatterns = [
    path('api_docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/users/', include('accounts.urls')),
]

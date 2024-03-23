from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename='')

app_name = 'accounts'

urlpatterns = [
    path('', include(router.urls)),
]
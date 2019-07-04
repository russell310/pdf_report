from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import DemoViewSet


router = routers.DefaultRouter()
router.register(r'demo', DemoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
from django.urls import path, include
from rest_framework import routers
from api.views import SensorReadingViewSet

router = routers.DefaultRouter()
router.register(r'sensor-reading', SensorReadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

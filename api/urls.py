from django.urls import path, include
from rest_framework import routers

from api.views import SensorReadingViewSet, SensorReadingCreateView

router = routers.DefaultRouter()
router.register(r'sensor-reading', SensorReadingViewSet)


urlpatterns = [
    path('routers/', include(router.urls)),
    path('sensor-reading-create/', SensorReadingCreateView.as_view(), name='sensor-reading-create'),
]

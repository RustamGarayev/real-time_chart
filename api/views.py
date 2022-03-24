from rest_framework import viewsets
from api.serializers import SensorReadingListSerializer
from core.models import SensorReading


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingListSerializer

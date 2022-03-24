from core.models import SensorReading
from api.serializers import SensorReadingListSerializer

# Rest Framework Imports
from rest_framework import status, viewsets, mixins
from rest_framework.views import APIView


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingListSerializer


class SensorReadingCreateView(APIView, mixins.CreateModelMixin):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingListSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

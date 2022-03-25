from core.models import SensorReading
from api.serializers import SensorReadingListSerializer

# Rest Framework Imports
from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingListSerializer


class SensorReadingCreateView(GenericAPIView, mixins.CreateModelMixin):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingListSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)

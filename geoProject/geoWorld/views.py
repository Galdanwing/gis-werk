from rest_framework import viewsets

from geoWorld.models import Municipality
from geoWorld.serializers import MunicipalitySerializer


class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

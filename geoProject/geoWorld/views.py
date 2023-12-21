from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter

from geoWorld.models import Municipality
from geoWorld.serializers import MunicipalitySerializer


class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    bbox_filter_field = "geometry"
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True

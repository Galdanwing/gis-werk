from rest_framework_gis import serializers

from .models import Municipality


class MunicipalitySerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Municipality
        fields = ["id", "name", "geometry"]

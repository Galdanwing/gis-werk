from django.contrib.gis.db import models


class Municipality(models.Model):
    name = models.CharField(max_length=256, unique=True)
    geometry = models.MultiPolygonField()

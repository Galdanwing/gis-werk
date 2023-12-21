from django.contrib.gis.db import models


class Municipality(models.Model):
    name = models.CharField(max_length=256, unique=True)
    geometry = models.MultiPolygonField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Municipalities"
        verbose_name = "Municipality"

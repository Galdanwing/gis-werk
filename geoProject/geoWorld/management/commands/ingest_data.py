import geopandas
from django.contrib.gis.geos import GEOSGeometry
from django.core.management import BaseCommand

from geoWorld.models import Municipality


class Command(BaseCommand):
    help = "Ingest geo data from dutch muncipalities into database"

    def add_arguments(self, parser):
        parser.add_argument("file_name", nargs=1, type=str)

    def handle(self, *args, **options):
        path_to_file = options["file_name"][0]
        gdf = geopandas.read_file(path_to_file)

        for index, row in gdf.iterrows():
            geos_multipolygon = GEOSGeometry(row["geometry"].wkt)
            Municipality.objects.create(name=row["name"], geometry=geos_multipolygon)

import geopandas
from django.contrib.gis.geos import GEOSGeometry
from django.core.management import BaseCommand
from rich.progress import Progress

from geoWorld.models import Municipality


class Command(BaseCommand):
    help = "Ingest geo data from Dutch municipalities into the database"

    def add_arguments(self, parser):
        parser.add_argument("file_name", nargs=1, type=str)

    def handle(self, *args, **options):
        path_to_file = options["file_name"][0]
        gdf = geopandas.read_file(path_to_file)

        total_rows = len(gdf)

        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=total_rows)

            for index, row in gdf.iterrows():
                geos_multipolygon = GEOSGeometry(row["geometry"].wkt)
                Municipality.objects.create(name=row["name"], geometry=geos_multipolygon)

                # Update progress
                progress.update(task, advance=1)

        self.stdout.write(self.style.SUCCESS("Data ingestion completed successfully."))

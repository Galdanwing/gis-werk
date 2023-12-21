from django.core.management import call_command
from django.test import TestCase

from geoWorld.models import Municipality


class IngestGeoDataTest(TestCase):
    def test_handle_command(self):
        # Call the management command with the temporary file
        call_command("ingest_data", "geoWorld/tests/data/example_muncipality.geojson")

        # Check if the Municipality object was created
        self.assertEqual(Municipality.objects.count(), 1)

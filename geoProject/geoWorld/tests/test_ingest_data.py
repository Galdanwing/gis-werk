import pytest
from django.core.management import call_command

from geoWorld.models import Municipality


@pytest.mark.django_db
def test_handle_command():
    # Call the management command with the temporary file
    call_command("ingest_data", "geoWorld/tests/data/example_muncipality.geojson")

    # Check if the Municipality object was created
    assert Municipality.objects.count() == 1

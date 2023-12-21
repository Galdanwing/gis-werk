from io import StringIO

import pytest
from django.core.management import call_command
from django.test import TestCase


@pytest.mark.django_db
class PendingMigrationsTests(TestCase):
    def test_no_pending_migrations(self):
        out = StringIO()
        try:
            call_command(
                "makemigrations",
                "--dry-run",
                "--check",
                stdout=out,
                stderr=StringIO(),
            )
        except SystemExit:
            raise AssertionError("Pending migrations:\n" + out.getvalue()) from None

# Generated by Django 5.0 on 2023-12-21 14:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("geoWorld", "0002_alter_municipality_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="municipality",
            options={"verbose_name": "Municipality", "verbose_name_plural": "Municipalities"},
        ),
    ]

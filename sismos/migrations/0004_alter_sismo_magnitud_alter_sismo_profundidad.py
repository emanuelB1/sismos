# Generated by Django 4.2.4 on 2023-08-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sismos", "0003_rename_depth_km_sismo_latitud_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sismo",
            name="magnitud",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="sismo",
            name="profundidad",
            field=models.FloatField(),
        ),
    ]
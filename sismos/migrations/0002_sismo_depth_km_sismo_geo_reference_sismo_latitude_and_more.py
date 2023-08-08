# Generated by Django 4.2.4 on 2023-08-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sismos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sismo",
            name="depth_km",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sismo",
            name="geo_reference",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sismo",
            name="latitude",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sismo",
            name="local_date",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sismo",
            name="longitude",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
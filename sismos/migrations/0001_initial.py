# Generated by Django 4.2.4 on 2023-08-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sismo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField()),
                ("profundidad", models.FloatField()),
                ("magnitud", models.FloatField()),
                ("ref_geografica", models.CharField(max_length=100)),
                ("latitud", models.FloatField()),
                ("longitud", models.FloatField()),
            ],
        ),
    ]

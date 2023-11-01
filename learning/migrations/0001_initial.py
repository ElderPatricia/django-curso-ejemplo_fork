# Generated by Django 4.2.6 on 2023-10-31 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
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
                ("nombre", models.CharField(max_length=120)),
                ("descripcion", models.TextField()),
                ("precio", models.IntegerField()),
                ("fecha_publicacion", models.DateField()),
            ],
        ),
    ]

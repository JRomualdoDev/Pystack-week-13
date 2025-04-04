# Generated by Django 5.1.7 on 2025-04-03 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentorados", "0002_rename_navigatos_mentorados_navigator"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disponibilidade",
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
                ("data_inicial", models.DateTimeField(blank=True, null=True)),
                ("agendado", models.BooleanField(default=False)),
                (
                    "mentor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorados.mentorados",
                    ),
                ),
            ],
        ),
    ]

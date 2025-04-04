# Generated by Django 5.1.7 on 2025-04-04 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentorados", "0006_alter_disponibilidadehorarios_mentor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reuniao",
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
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("G", "Gestão"),
                            ("M", "Marketing"),
                            ("RH", "Gestão de pessoas"),
                            ("I", "Impostos"),
                        ],
                        max_length=2,
                    ),
                ),
                ("descricao", models.TextField()),
                (
                    "data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorados.disponibilidadehorarios",
                    ),
                ),
                (
                    "mentorado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorados.mentorados",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-02 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mentorados", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mentorados",
            old_name="navigatos",
            new_name="navigator",
        ),
    ]

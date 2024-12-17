# Generated by Django 5.1 on 2024-12-17 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_itenscompra"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itenscompra",
            name="pedido",
        ),
        migrations.AddField(
            model_name="itenscompra",
            name="produtos",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.produto"
            ),
        ),
    ]

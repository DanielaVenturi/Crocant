# Generated by Django 5.0.6 on 2024-08-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_remove_pedido_categoria_produto_categoria"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pedido",
            options={"verbose_name": "Pedido", "verbose_name_plural": "Pedidos"},
        ),
        migrations.AddField(
            model_name="produto",
            name="tamanho",
            field=models.PositiveIntegerField(
                blank=True,
                choices=[
                    (33, "33"),
                    (34, "34"),
                    (35, "35"),
                    (36, "36"),
                    (37, "37"),
                    (38, "38"),
                    (39, "39"),
                    (40, "40"),
                    (41, "41"),
                    (42, "42"),
                    (43, "43"),
                    (44, "44"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="produto",
            field=models.ManyToManyField(blank=True, null=True, related_name="pedidos", to="core.produto"),
        ),
    ]
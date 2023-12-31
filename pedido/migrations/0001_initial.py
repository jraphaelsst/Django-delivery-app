# Generated by Django 4.1.4 on 2023-05-07 14:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
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
                ("usuario", models.CharField(max_length=200)),
                ("total", models.FloatField()),
                ("troco", models.CharField(blank=True, max_length=20)),
                ("pagamento", models.CharField(blank=True, max_length=20)),
                ("ponto_referencia", models.CharField(blank=True, max_length=2000)),
                (
                    "data",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 5, 7, 11, 33, 47, 183298)
                    ),
                ),
                ("cep", models.CharField(blank=True, max_length=50)),
                ("rua", models.CharField(max_length=200)),
                ("numero", models.CharField(max_length=10)),
                ("bairro", models.CharField(blank=True, max_length=200)),
                ("telefone", models.CharField(max_length=30)),
                ("entregue", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ItemPedido",
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
                ("quantidade", models.IntegerField()),
                ("preco", models.FloatField()),
                ("descricao", models.TextField()),
                ("adicionais", models.TextField()),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pedido.pedido"
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.produto"
                    ),
                ),
            ],
        ),
    ]

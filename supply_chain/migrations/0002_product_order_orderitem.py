# Generated by Django 4.2.11 on 2024-04-02 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0002_remove_product_order_hotel_delete_orderitem_and_more"),
        ("supply_chain", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="product_order",
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
                ("order_date", models.DateField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("placed", "Placed"),
                            ("in_warehouse", "In Warehouse"),
                            ("packed", "Order Packed"),
                            ("out_of_delivery", "Out Of Delivery"),
                        ],
                        default="Placed",
                        max_length=20,
                    ),
                ),
                ("total_amount", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel.hotel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supply_chain.product_order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supply_chain.product",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-31 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("book_id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("inventory", models.IntegerField()),
            ],
            options={
                "db_table": "Books",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "Users",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("order_id", models.IntegerField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                ("total_price", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "book_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.books"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.users"
                    ),
                ),
            ],
            options={
                "db_table": "Orders",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Payments",
            fields=[
                ("payment_id", models.IntegerField(primary_key=True, serialize=False)),
                ("payment_method", models.CharField(max_length=255)),
                ("payment_date", models.DateField()),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.orders"
                    ),
                ),
            ],
            options={
                "db_table": "Payments",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ShoppingCart",
            fields=[
                (
                    "shopping_cart_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("quantity", models.IntegerField()),
                (
                    "book_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.books"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.users"
                    ),
                ),
            ],
            options={
                "db_table": "ShoppingCart",
                "managed": True,
            },
        ),
    ]
# Generated by Django 5.2.1 on 2025-05-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_is_new"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["-is_new", "name"],
                "verbose_name": "商品",
                "verbose_name_plural": "商品",
            },
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-15 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_remove_cart_subtotal'),
        ('orders', '0004_alter_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.cart'),
        ),
    ]
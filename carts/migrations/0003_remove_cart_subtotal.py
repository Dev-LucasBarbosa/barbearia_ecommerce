# Generated by Django 5.1 on 2024-09-14 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
    ]
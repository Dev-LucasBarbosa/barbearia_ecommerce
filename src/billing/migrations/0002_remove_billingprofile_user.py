# Generated by Django 5.1 on 2024-10-04 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofile',
            name='user',
        ),
    ]
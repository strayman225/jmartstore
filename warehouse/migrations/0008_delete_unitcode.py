# Generated by Django 3.2.23 on 2023-11-28 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_remove_stock_unitcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UnitCode',
        ),
    ]

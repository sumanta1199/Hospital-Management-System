# Generated by Django 3.2.5 on 2022-04-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_orders_orderupdate_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

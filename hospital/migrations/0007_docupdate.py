# Generated by Django 3.2.5 on 2021-12-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20211222_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='docupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'docupdate',
            },
        ),
    ]

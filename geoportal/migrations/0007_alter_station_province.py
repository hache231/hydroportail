# Generated by Django 5.1.4 on 2024-12-20 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0006_rename_opening_hours_station_opening_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoportal.provinces'),
        ),
    ]

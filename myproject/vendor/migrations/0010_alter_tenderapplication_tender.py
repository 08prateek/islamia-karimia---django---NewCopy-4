# Generated by Django 5.0.6 on 2024-07-20 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_tenderapplication_tender_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderapplication',
            name='tender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.tender'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forarmenians_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiclead",
            name="power",
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]

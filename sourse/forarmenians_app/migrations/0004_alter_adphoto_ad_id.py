# Generated by Django 4.1.5 on 2023-01-06 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("forarmenians_app", "0003_rename_model_vehiclebrand_brand_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adphoto",
            name="ad_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="forarmenians_app.ad",
            ),
        ),
    ]

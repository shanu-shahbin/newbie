# Generated by Django 5.1.1 on 2024-09-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_company_location_company_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='carrier_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

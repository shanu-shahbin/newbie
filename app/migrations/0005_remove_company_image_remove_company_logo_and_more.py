# Generated by Django 5.1.1 on 2024-09-30 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_company_carrier_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='image',
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_footer_whatsapp_channel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='telegram_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

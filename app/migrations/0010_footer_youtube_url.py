# Generated by Django 5.1.1 on 2024-09-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_footer_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

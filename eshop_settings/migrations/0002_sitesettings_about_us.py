# Generated by Django 3.2.5 on 2021-08-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ما'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0001_initial'),
        ('eshop_products', '0003_auto_20210811_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory', verbose_name='دسته بندی'),
        ),
    ]

# Generated by Django 4.1 on 2022-08-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_color_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='product.color'),
        ),
    ]

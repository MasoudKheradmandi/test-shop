# Generated by Django 4.1 on 2022-09-10 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_takhfif'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tedad_mahsole',
            field=models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد فروش'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-07 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_takhfif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='takhfif',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='درصد تخفیف'),
        ),
    ]

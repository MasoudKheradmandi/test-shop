# Generated by Django 4.0.6 on 2022-08-30 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_color_options_alter_size_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='takhfif',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='درصد تخفیف'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_footerzir_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabligh',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]

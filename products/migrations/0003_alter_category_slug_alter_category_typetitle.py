# Generated by Django 5.1.1 on 2024-10-15 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_slug_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='typeTitle',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.type'),
        ),
    ]
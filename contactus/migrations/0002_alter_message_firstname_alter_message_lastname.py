# Generated by Django 5.1.1 on 2024-10-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='firstName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='lastName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

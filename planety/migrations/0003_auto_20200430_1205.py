# Generated by Django 3.0.5 on 2020-04-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planety', '0002_auto_20200430_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discovery',
            name='discovery_date',
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='discovery_date',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, verbose_name='Discovery date'),
        ),
    ]
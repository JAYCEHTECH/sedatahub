# Generated by Django 4.2.4 on 2025-01-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0017_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afaregistration',
            name='occupation',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='afaregistration',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

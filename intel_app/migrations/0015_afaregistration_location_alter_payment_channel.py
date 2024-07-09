# Generated by Django 5.0 on 2024-01-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0014_agentbigtimebundleprice_bigtimebundleprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afaregistration',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='channel',
            field=models.CharField(blank=True, choices=[('mtn', 'mtn'), ('ishare', 'ishare'), ('bigtime', 'bigtime'), ('afa', 'afa'), ('topup', 'topup')], max_length=250, null=True),
        ),
    ]

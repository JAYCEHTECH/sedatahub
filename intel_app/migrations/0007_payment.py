# Generated by Django 4.1 on 2023-06-07 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0006_isharebundleprice_mtnbundleprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=256)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('payment_description', models.CharField(blank=True, max_length=500, null=True)),
                ('transaction_status', models.CharField(blank=True, max_length=256, null=True)),
                ('transaction_date', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

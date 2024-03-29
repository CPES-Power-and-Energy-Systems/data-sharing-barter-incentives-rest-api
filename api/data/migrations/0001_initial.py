# Generated by Django 3.2 on 2024-02-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketForecasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('request', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(choices=[('w', 'Watt'), ('kw', 'Kilo Watt'), ('mw', 'Mega Watt')], max_length=2)),
                ('registered_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'market_forecasts',
            },
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('forecasts', 'Forecast'), ('measurements', 'Measurement')], max_length=12)),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(choices=[('w', 'Watt'), ('kw', 'Kilo Watt'), ('mw', 'Mega Watt')], max_length=2)),
                ('time_interval', models.IntegerField(choices=[('5', 'T5'), ('15', 'T15'), ('30', 'T30'), ('60', 'T60')])),
                ('aggregation_type', models.CharField(choices=[('avg', 'Avg')], max_length=3)),
                ('registered_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'raw_data',
            },
        ),
    ]

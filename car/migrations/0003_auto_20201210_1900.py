# Generated by Django 3.0.7 on 2020-12-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20201124_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordr',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('park_id', models.IntegerField(primary_key=True, serialize=False)),
                ('park_block', models.CharField(blank=True, max_length=50, null=True)),
                ('park_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_address', models.CharField(blank=True, max_length=50, null=True)),
                ('station_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_contact', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'managed': False},
        ),
    ]

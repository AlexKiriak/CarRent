# Generated by Django 3.0.7 on 2020-12-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordr',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_username', models.TextField(blank=True, null=True)),
                ('order_usercontacts', models.TextField(blank=True, null=True)),
                ('order_carname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ordr',
                'managed': False,
            },
        ),
    ]

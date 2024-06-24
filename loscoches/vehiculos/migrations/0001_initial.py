# Generated by Django 5.0.6 on 2024-06-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.IntegerField()),
                ('referencia', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('valor_comercial', models.BigIntegerField()),
            ],
        ),
    ]

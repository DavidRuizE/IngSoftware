# Generated by Django 4.1.2 on 2024-03-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('producto1', models.CharField(max_length=50)),
                ('producto2', models.CharField(max_length=50)),
                ('producto3', models.CharField(max_length=50)),
                ('producto4', models.CharField(max_length=50)),
            ],
        ),
    ]
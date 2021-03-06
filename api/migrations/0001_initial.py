# Generated by Django 4.0.4 on 2022-05-18 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('date', models.DateField()),
                ('salary', models.FloatField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('birtday', models.DateField()),
            ],
        ),
    ]

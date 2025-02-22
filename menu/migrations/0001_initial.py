# Generated by Django 4.2 on 2023-05-10 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('PID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=9999)),
                ('description', models.CharField(max_length=9999)),
                ('spicy', models.BooleanField()),
                ('vegan', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaToppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza')),
            ],
        ),
    ]

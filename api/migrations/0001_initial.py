# Generated by Django 4.2.2 on 2023-06-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Reteta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=128)),
                ('timp_preparare', models.IntegerField()),
                ('portii', models.IntegerField()),
                ('ingrediente', models.ManyToManyField(to='api.ingredient')),
            ],
        ),
    ]

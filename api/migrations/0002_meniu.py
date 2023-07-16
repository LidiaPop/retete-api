# Generated by Django 4.2.2 on 2023-07-16 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meniu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=128)),
                ('aperitiv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reteta_aperitive', to='api.reteta')),
                ('desert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reteta_deserturi', to='api.reteta')),
                ('fel_principal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reteta_feluri_principale', to='api.reteta')),
            ],
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-26 21:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now)),
                ('fecha_fin', models.DateField(default=datetime.datetime.now)),
                ('estado', models.CharField(choices=[('Planificado', 'Planificado'), ('En Curso', 'En Curso'), ('Finalizado', 'Finalizado')], default='Planificado', max_length=11)),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas', to='Projects.lider')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetas', to='Projects.sponsor')),
            ],
        ),
    ]

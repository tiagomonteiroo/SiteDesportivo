# Generated by Django 5.0.4 on 2024-05-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubehome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('main', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Avançado', 'Avançado'), ('Extremo', 'Extremo'), ('Médio', 'Médio'), ('Central', 'Central'), ('Lateral', 'Lateral'), ('Guarda-Redes', 'Guarda-Redes')], max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-07 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('palavra_passe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Treinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ID_prod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('desporto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('conta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.conta')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=100)),
                ('ano_entrada', models.DateField()),
            ],
            bases=('clubehome.conta',),
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('conta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.conta')),
                ('nome', models.CharField(max_length=100)),
                ('NIF', models.IntegerField()),
                ('nascimento', models.DateField()),
            ],
            bases=('clubehome.conta',),
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('treinador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.treinador')),
            ],
            bases=('clubehome.treinador',),
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('treinador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.treinador')),
            ],
            bases=('clubehome.treinador',),
        ),
        migrations.CreateModel(
            name='Bilhete',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.produto')),
                ('data', models.DateField()),
                ('lugar', models.IntegerField()),
                ('N_Emissao', models.IntegerField()),
            ],
            bases=('clubehome.produto',),
        ),
        migrations.CreateModel(
            name='Merchandising',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.produto')),
                ('tipo', models.CharField(max_length=100)),
            ],
            bases=('clubehome.produto',),
        ),
        migrations.AddField(
            model_name='treinador',
            name='plantel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubehome.plantel'),
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('posicao', models.CharField(choices=[('Avançado', 'Avançado'), ('Extremo', 'Extremo'), ('Médio', 'Médio'), ('Central', 'Central'), ('Lateral', 'Lateral'), ('Guarda-Redes', 'Guarda-Redes')], max_length=20)),
                ('idade', models.IntegerField()),
                ('plantel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubehome.plantel')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('utilizador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clubehome.utilizador')),
                ('N_Socio', models.IntegerField()),
                ('is_socio', models.BooleanField()),
            ],
            bases=('clubehome.utilizador',),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubehome.produto')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubehome.utilizador')),
            ],
        ),
    ]
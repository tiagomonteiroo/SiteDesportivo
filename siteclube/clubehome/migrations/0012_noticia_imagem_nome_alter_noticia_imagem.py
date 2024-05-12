# Generated by Django 5.0.4 on 2024-05-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubehome', '0011_product_imagem_nome_alter_product_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagem_nome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='clubehome/static/'),
        ),
    ]
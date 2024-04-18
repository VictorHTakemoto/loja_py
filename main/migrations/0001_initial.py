# Generated by Django 5.0.3 on 2024-04-11 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponivel', models.BooleanField(default=True)),
                ('estoque', models.PositiveIntegerField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(blank=True, upload_to='produtos/%y/%m/%d')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='main.categoria')),
            ],
            options={
                'ordering': ('nome',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
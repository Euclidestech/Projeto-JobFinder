# Generated by Django 4.2.1 on 2023-07-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=8)),
                ('sexo', models.TextField(default='nao definido')),
                ('experiencias', models.TextField(default='sem experiencia')),
                ('rua', models.TextField(max_length=10, null=True)),
                ('bairro', models.TextField(max_length=10, null=True)),
                ('cidade', models.TextField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id_vaga', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]

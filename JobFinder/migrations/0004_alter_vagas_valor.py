# Generated by Django 4.2.1 on 2023-07-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobFinder', '0003_alter_vagas_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='valor',
            field=models.TextField(default=0),
        ),
    ]

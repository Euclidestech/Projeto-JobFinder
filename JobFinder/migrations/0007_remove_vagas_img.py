# Generated by Django 4.2.1 on 2023-07-22 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobFinder', '0006_vagas_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagas',
            name='img',
        ),
    ]

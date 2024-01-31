# Generated by Django 4.2.5 on 2023-09-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('cpf', models.TextField(max_length=11)),
                ('endereco', models.TextField(max_length=255)),
                ('cep', models.TextField(max_length=255)),
                ('cidade', models.TextField(max_length=255)),
                ('estado', models.TextField(max_length=2)),
            ],
        ),
    ]
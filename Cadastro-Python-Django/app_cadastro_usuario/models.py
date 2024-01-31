from django.db import models

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    cpf = models.TextField(max_length=11)
    endereco = models.TextField(max_length=255)
    cep = models.TextField(max_length=255)
    cidade = models.TextField(max_length=255)
    estado = models.TextField(max_length=2)
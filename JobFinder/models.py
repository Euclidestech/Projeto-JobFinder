from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=8)
    sexo = models.TextField(default="nao definido")
    experiencias = models.TextField(default="sem experiencia")
    rua = models.TextField(max_length=10, null=True)
    bairro = models.TextField(max_length=10,null=True)
    cidade = models.TextField(max_length=10,null=True)
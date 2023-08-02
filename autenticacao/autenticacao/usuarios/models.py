from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Unidade(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    url_imagem = models.URLField(max_length=400, null=False, default="")
    objects = models.Manager()

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True)

    def pegar_url_reversa(self):
        return reverse('post_detail', args=[self.pk])

    def __str__(self):
        return self.email
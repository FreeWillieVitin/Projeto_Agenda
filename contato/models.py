"""
Documentação dos models: https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
Documentação sobre tipos de dados Django: https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices
"""
from django.db import models
from django.utils import timezone
# Create your models here.


class Contato(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    data_contato = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'

"""
Documentação dos models: https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
Documentação sobre tipos de dados Django: https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    # Uma das funções da classe meta é controlar o nome que é exibido para as tabelas admin e como elas se relacionam com um ou
    # mais dados ou seja verbose_name é o nome da tabela para 1 dado, verbose_name_plural é quando tem vários dados
    # Vídeo sobre traduções Django: https://www.youtube.com/watch?v=iIsLwz_vkzA
    # Documentação da classe Meta Django: https://docs.djangoproject.com/pt-br/4.2/ref/models/options/
    #
    # class Meta:
    #     verbose_name = 'Categoria'
    #     verbose_name_plural = 'Varias'

    desc_categ = models.CharField(max_length=50)

    # def __str__(self) -> str:
    #     return 'ABC'


class Contato(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    data_contato = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    mostra = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    cod_categ = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, blank=True, null=True
    )
    proprietario = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'

from django.contrib import admin
from contato.models import Contato, Categoria
# Register your models here.


@admin.register(Contato)
class AdminContato(admin.ModelAdmin):
    # Campos que seão mostrados no admin do django
    list_display = ['id', 'f_name', 'l_name',
                    'telefone', 'cod_categ', 'mostra']
    # Ordena em ordem crescente, se colocar um sinal - na frente do campo no caso o id será decrescente, essas variavéis tem que
    # tem o nome exatamente como está sendo mostrado caso contrário o DJango não reconhece
    ordering = ['id',]
    list_filter = ['data_contato',]  # Adiciona um filtro na tela de admin
    # Adiciona um campo de busca, esse campo somente busca pelos campos adicionado na lista
    search_fields = ['f_name', 'l_name',]
    list_per_page = 20  # Quantidade de registros por página
    # Quantidade máxima de registros necessários para utilizar a função mostrar todos os registros
    list_max_show_all = 200
    # Define quais campos podem ser editados na aréa de mostra de registros
    list_editable = ['f_name', 'l_name', 'mostra']
    # Define uma coluna como link para ter acesso rapido a aréa de administração do registro
    list_display_links = ['id',]


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ['desc_categ',]
    ordering = ['id',]

from django.urls import path
from contato.views import index, descricao, search

app_name = 'contato'

# Na lista abaixo criamos as urls, que fazm o link diretamente com as views entregando a informação a view realizar a requisição
# servidor.
urlpatterns = [
    path('<int:contact_id>/', descricao, name='descricao'),
    path('search/', search, name='search'),
    path('', index, name='index'),
]

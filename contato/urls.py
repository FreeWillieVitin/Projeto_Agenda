from django.urls import path
from contato.views import index, descricao, search, create

app_name = 'contato'

# Na lista abaixo criamos as urls, que fazm o link diretamente com as views entregando a informação a view realizar a requisição
# servidor.
urlpatterns = [
    path('search/', search, name='search'),
    path('', index, name='index'),

    # CRUD, a seguir temos um padrão que geralmente indicado para URLs em que o conteúdo é um CRUD
    path('<int:contact_id>/detail/', descricao, name='descricao'),
    path('create/', create, name='create'),
    # path('<int:contact_id>/update/', descricao, name='descricao'),
    # path('<int:contact_id>/delete/', descricao, name='descricao'),


]

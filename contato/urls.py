from django.urls import path
from contato.views import index, descricao

app_name = 'contato'

# Na lista abaixo criamos as urls, que fazm o link diretamente com as views entregando a informação a view realizar a requisição
# servidor.
urlpatterns = [
    path('', index, name='index'),
    path('<int:contato_id>/', descricao, name='descricao'),
]

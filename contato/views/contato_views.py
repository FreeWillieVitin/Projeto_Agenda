from django.shortcuts import render
from contato.models import Contato

# Create your views here.


# Criação de uma view, é basicamente o que envia a requisição para o servidor de quais informações serão acessadas, no caso abaixo
# teremos alguns filtros, um deles exibe apenas os registros que estão mesmo marcados para serem exibidos pelo administrador
# e o outro filtro é de ordem, coluna com sinal negativo significa ordem decrescente
def index(request):
    contatos = Contato.objects\
        .filter(mostra=True)\
        .order_by('-id')

    # print(contatos.query)

    contexto = {
        'contatos': contatos,
    }

    return render(
        request,
        'contato/index.html',
        contexto,
    )


def descricao(request, contato_id):
    desc_contato = Contato.objects.get(
        id=contato_id)  # .get busca um único valor
    # print(contatos.query)

    contexto2 = {
        'descricao': desc_contato,
    }

    return render(
        request,
        'contato/desc_contato.html',
        contexto2,
    )

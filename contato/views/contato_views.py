from django.shortcuts import render, get_object_or_404
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
        'nome_contato': 'Contato - '
    }

    return render(
        request,
        'contato/index.html',
        contexto,
    )


def descricao(request, contact_id):
    # desc = Contato.objects.get(
    #     id=contact_id)  # .get busca um único valor

    # Função pronta para checar se algo existe, caso contrário levanta uma exceção
    desc = get_object_or_404(Contato.objects, id=contact_id, mostra=True)

    nome = f'{desc.f_name} - '

    contexto1 = {
        'desc': desc,
        'nome_contato': nome
    }

    return render(
        request,
        'contato/desc_contato.html',
        contexto1,
    )

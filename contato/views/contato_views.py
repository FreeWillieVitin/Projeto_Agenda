from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato
from django.db.models import Q

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
        'nome_contato': 'Search - '
    }

    return render(
        request,
        'contato/index.html',
        contexto,
    )

# Essa view de busca faz um tipo de configuração para o navegador ignorar certos tipos de buscas, por exemplo ao usar
# a função strip padrão do python ignoramos qualquer espaço em branco que seja colocado no campo de busca pelo usuário, aceitando
# apenas valores com caracteres, o get é para receber o valor que vem do name 'q' definido no template que contém as tags do input
# de busca, além disso podemos usar uma função do django para que se o usuário digite alguma sequência de caracteres seja
# redicionado para outro lugar, no caso se realizar uma busca em branco a função redirect encaminha para a home da página.

# https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups - Define os filtros para realizar as buscas


def search(request):
    valor_busca = request.GET.get('q', '').strip()
    print(valor_busca)

    if valor_busca == "":
        return redirect('contato:index')

    contatos = Contato.objects\
        .filter(mostra=True)\
        .filter(
            Q(f_name__icontains=valor_busca) |
            Q(l_name__icontains=valor_busca) |
            Q(email__icontains=valor_busca) |
            Q(telefone__icontains=valor_busca)
        )\
        .order_by('-id')

    # print(contatos.query)

    contexto = {
        'contatos': contatos,
        'nome_contato': 'Contato - ',
        'valor_busca': valor_busca
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

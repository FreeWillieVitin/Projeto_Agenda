from django.shortcuts import render

# Create your views here.


# Criação de uma view, é basicamente o que envia a requisição para o servidor de quais informações serão acessadas
def index(request):
    return render(
        request,
        'contato/index.html',
    )

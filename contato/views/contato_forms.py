from django.shortcuts import render, get_object_or_404
from contato.views.forms import FormContato
from django.db.models import Q


def create(request):
    if request.method == 'POST':
        contexto = {
            'form': FormContato(data=request.POST)
        }

        return render(
            request,
            'contato/create.html',
            contexto,
        )

    contexto = {
        'form': FormContato()
    }

    return render(
        request,
        'contato/create.html',
        contexto,
    )

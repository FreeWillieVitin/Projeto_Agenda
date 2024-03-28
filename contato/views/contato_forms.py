from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato
from django.db.models import Q


def create(request):
    contexto = {

    }

    return render(
        request,
        'contato/create.html',
        contexto,
    )

from django.shortcuts import render
from .models import Produto



# Create your views here.

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'core.html', context)


def contact(request):
    return render(request, 'core/contato.html')
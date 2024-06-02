from django.shortcuts import render



# Create your views here.

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contato.html')
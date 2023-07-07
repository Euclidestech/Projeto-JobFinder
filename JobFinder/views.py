from django.shortcuts import render
from .models import Usuarios



def index(request):
    return render(request, 'telas/index.html')
def cadastro(request):
    return render(request, 'telas/cadastro.html')
def cadastroEmpresa(request):
    return render(request, 'telas/cadastro_empresa.html')
def escolha(request):
    return render(request, 'telas/escolha.html')
def batepapo(request):
    return render(request, 'telas/batepapo.html')
def feed(request):
    return render(request,'telas/feed.html')
def usuarios(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.sexo = request.POST.get('sexo')
    novo_usuario.experiencias = request.POST.get('experiencias')
    novo_usuario.rua = request.POST.get('rua')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.cidade = request.POST.get('cidade')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    
    return render(request,'telas/usuarios.html',usuarios)

    
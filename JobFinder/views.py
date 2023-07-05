from django.shortcuts import render



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
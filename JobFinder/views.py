from django.shortcuts import render



def index(request):
    return render(request, 'telas/index.html')
def cadastro(request):
    return render(request, 'telas/cadastro.html')
def feed(request):
    return render(request,'telas/feed.html')
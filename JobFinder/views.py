from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Usuarios,Vagas
from django.views.generic.edit import DeleteView


def index(request):
    return render(request, 'telas/index.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'telas/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        novo_usuario = Usuarios()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.sexo = request.POST.get('sexo')
        novo_usuario.experiencias = request.POST.get('experiencias')
        novo_usuario.rua = request.POST.get('rua')
        novo_usuario.bairro = request.POST.get('bairro')
        novo_usuario.cidade = request.POST.get('cidade')
        
        
        
        user =  User.objects.filter(username =nome).first()
    if user:
        return HttpResponse('ja existe usuario')
    else:
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()
        novo_usuario.save()
        usuarios = {
        'usuarios': Usuarios.objects.all()
         }
        return HttpResponse('usuario cadastrado')
       
    
        

def login(request):
    if request.method == "GET":
        return render(request,'telas/index.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = authenticate(username = usuario, password= senha)
        
    if user:
     login_django(request,user)
     vagas = {
                'vagas': Vagas.objects.all()
                }  
     return render(request,'telas/feed.html',vagas)
    else:
        print = {
            'print': "Credenciais invalidas"
        }
        return render(request,'telas/index.html',print)
            #  return HttpResponse ('Usuario ou senha invalidos')

def cadastroEmpresa(request):
    return render(request, 'telas/cadastro_empresa.html')
def escolha(request):
    return render(request, 'telas/escolha.html')
def batepapo(request):
    return render(request, 'telas/batepapo.html')
@login_required(login_url="/index/")
def feed(request):
    vagas = {
        'vagas': Vagas.objects.all()
        }
    return render(request,'telas/feed.html',vagas)

def cadastrar_vaga(request):
    nova_vaga = Vagas()
    nova_vaga.descricao = request.POST.get('job-description') 
    if request.POST.get('valor') == '':
        nova_vaga.valor = "A Combinar"
    else:
         valor = request.POST.get('valor')
         nova_vaga.valor ="R$ " + valor+",00"
    # nova_vaga.img = request.POST.get('img')
    if nova_vaga.descricao == '':
        vagas = {
            'vagas': Vagas.objects.all()
            }
        return render(request,'telas/feed.html',vagas)
    else:
        nova_vaga.save()
        vagas = {
            'vagas': Vagas.objects.all()
            }
        return render(request,'telas/feed.html',vagas)
    
    
    
def delete_vaga(request,id):
    item = get_object_or_404(Vagas,pk=id)
    item.delete()
    
    vagas = {
            'vagas': Vagas.objects.all()
            }
    return render(request,'telas/feed.html',vagas)
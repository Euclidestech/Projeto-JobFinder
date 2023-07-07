from django.urls import path
from JobFinder.views import index, cadastro, feed,cadastroEmpresa,escolha,batepapo,usuarios

urlpatterns = [
  path('', index,name='index'),
  path('cadastro/', cadastro, name='cadastro'),
  path('feed/', feed, name='feed'),
  path('cadastro_empresa',cadastroEmpresa,name='cadastro_empresa'),
  path('escolha',escolha,name='escolha'),
  path('batepapo',batepapo,name='batepapo'),
  path('usuario/', usuarios,name='usuario_cadastrado')
]
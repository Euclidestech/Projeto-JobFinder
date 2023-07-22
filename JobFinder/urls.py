from django.urls import path
from . import views
from JobFinder.views import index,cadastrar_vaga ,feed,cadastro,cadastroEmpresa,escolha,batepapo,delete_vaga
urlpatterns = [
  path('', index,name='index'),
  path('login/', views.login,name="index"),
  path('cadastro/', cadastro, name='cadastro'),
  # path('cadastro/', usuarios, name='cadastro'),
  path('feed/', feed, name='feed'),
  path('cadastro_empresa',cadastroEmpresa,name='cadastro_empresa'),
  path('escolha',escolha,name='escolha'),
  path('batepapo',batepapo,name='batepapo'),
  # path('usuario/', usuarios,name='usuario_cadastrado'),
  path('cadastrar/',cadastrar_vaga, name='cadastrar_vaga'),
  path('delete/<int:id>/',views.delete_vaga, name="delete")
]
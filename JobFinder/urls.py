from django.urls import path
from JobFinder.views import index, cadastro, feed

urlpatterns = [
  path('', index,name='index'),
  path('cadastro/', cadastro, name='cadastro'),
  path('feed/', feed, name='feed')
]
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.tela_inicial, name="tela_inicial"),
    path('cadastro_entrada/', views.cadastro_entrada, name="cadastro_entrada"),
    path('cadastro_saida/', views.cadastro_saida, name="cadastro_saida"),
    path('listar_registros/', views.listar_registros.as_view(), name="listar_registros"),
]

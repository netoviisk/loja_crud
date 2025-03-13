"""
URL configuration for loja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),

    path('listas/lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('listas/lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('listas/lista_produtos/', views.lista_produtos, name='lista_produtos'),

    path('cadastro/cadastro_clientes', views.cadastro_clientes, name='cadastro_clientes'),
    path('cadastro/cadastro_pedidos', views.cadastro_pedidos, name='cadastro_pedidos'),
    path('cadastro/cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos'),

    path('atualiza_deleta/atualiza_clientes/<int:clientes_id>/', views.atualiza_clientes, name='atualiza_clientes'),
    path('atualiza_deleta/atualiza_pedidos/<int:pedidos_id>/', views.atualiza_pedidos, name='atualiza_pedidos'),
    path('atualiza_deleta/atualiza_produtos/<int:produtos_id>/', views.atualiza_produtos, name='atualiza_produtos'),
]

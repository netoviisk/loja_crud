from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Pedidos, Produtos
from .forms import ClientesForms, PedidosForms, ProdutosForms

def home(request):
    return render(request, 'home.html')

#------==CADASTRO==------#

def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClientesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClientesForms()
    return render(request, 'cadastro/cadastro_clientes.html', {'form': form})

def cadastro_pedidos(request):
    if request.method == "POST":
        form = PedidosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidosForms
    return render(request, 'cadastro/cadastro_pedidos.html', {'form': form})

def cadastro_produtos(request):
    if request.method == "POST":
        form = ProdutosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutosForms
    return render(request, 'cadastro/cadastro_produtos.html', {'form': form})


#------==LISTAS==------#

def lista_clientes(request):
    clientes=Clientes.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def lista_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


# ------==ATUALIZA==------#

def atualiza_clientes(request, clientes_id):
    clientes = get_object_or_404(Clientes, id=clientes_id)
    if request.method == 'POST':
        form = ClientesForms(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('Lista_clientes')
    else:
        form = ClientesForms(instance=clientes)
    return render(request, 'atualiza_deleta/atualizar_clientes.html', {'form': form, 'clientes': clientes})

def atualiza_pedidos(request, pedidos_id):
    pedidos = get_object_or_404(Pedidos, id=pedidos_id)
    if request.method == 'POST':
        form = PedidosForms(request.POST, instance=pedidos)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidosForms(instance=pedidos)
    return render(request, 'atualiza_deleta/atualizar_pedidos.html', {'form': form, 'pedidos': pedidos})

def atualiza_produtos(request, produtos_id):
    produtos = get_object_or_404(Produtos, id=produtos_id)
    if request.method == 'POST':
        form = ProdutosForms(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutosForms(instance=produtos)
    return render(request, 'atualiza_deleta/atualizar_produtos.html', {'form': form, 'produtos': produtos})

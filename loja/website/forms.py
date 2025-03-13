from django import forms
from .models import Clientes, Produtos, Pedidos

class ClientesForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = {'cli_nome', 'cli_email', 'cli_telefone'}

class ProdutosForms(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = {'pro_nome', 'pro_descricao', 'pro_preco'}

class PedidosForms(forms.ModelForm):
    class Meta:
        model = Pedidos
        field = {'ped_data'}
        exclude ={'ped_id_produtos', 'ped_id_clientes'}

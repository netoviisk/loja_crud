from django.db import models

class Clientes(models.Model):
    cli_nome = models.CharField(max_length=100, verbose_name="Nome de Cliente")
    cli_email = models.CharField(max_length=100, verbose_name="E-mail")
    cli_telefone = models.CharField(max_length=20, verbose_name="Número de Telefone")

    def __str__(self):
        return self.cli_nome

class Produtos(models.Model):
    pro_nome = models.CharField(max_length=100, verbose_name="Nome de Produto")
    pro_descricao = models.CharField(max_length=1000, verbose_name="Descrição de Produto")
    pro_preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Produto")

    def __str__(self):
        return self.pro_nome

class Pedidos(models.Model):
    ped_data = models.DateTimeField(verbose_name="Data do Pedido")
    ped_id_produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True, blank=True)
    ped_id_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.ped_data)

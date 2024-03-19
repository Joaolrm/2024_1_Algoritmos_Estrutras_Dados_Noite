from Produto import *
class Pedido:

    def __init__(self, pessoa):
        self.id = int
        self.end = str
        self.produtos = []
        self.cliente = pessoa
        

    def addproduto(self, produto):
        self.produtos.append(produto)
        soma_pedido = 0
        for x in self.produtos:
            soma_pedido += x.preco
        return soma_pedido
            

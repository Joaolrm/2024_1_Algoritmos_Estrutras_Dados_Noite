from Produto import Produto
from Pessoa import Pessoa

class Pedido:

    def __init__(self, end, cliente = Pessoa("Anônimo")):
        self.id = None
        self.end = end
        self.cliente = cliente
        self.produtos = []
        

    def addproduto(self, prod):
        self.produtos.append(prod)
        soma_pedido = 0
        for x in self.produtos:
            soma_pedido += x.preco
        return soma_pedido
            
    def __str__(self):
        texto = f"""
            Endereço do Pedido: {self.end} - {self.cliente.cidade.nome}
            Cliente: {self.cliente.nome}
            Produtos:
        """
        if len(self.produtos) == 0:
            texto += "      Pedido Vazio"

        for p in self.produtos:
            texto += f"{p.nome} - {str(p.preco)} - Cat: {p.cat.nome}\n"
        return texto


from Categoria import Categoria

class Produto:
    def __init__(self, nome, preco = 10.00, qtd = 0,cat=Categoria()):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.cat = cat

    def __str__(self) :
        texto = f"""Produto: {self.nome}
        Preço: {str(self.preco)}
        Categoria: {self.cat.nome}"""
        return texto
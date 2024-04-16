from Categoria import Categoria


class Veiculo():

    def __init__(self, marca = "Honda", ano = 2014, cat = Categoria(None)):
        self.id = None 
        self.marca = marca
        self.ano = ano
        self.categoria = cat

    def __str__(self):
        texto =f"""
        Marca: {self.marca}
        Ano: {self.ano}
        Categoria: {self.categoria.nome}"""
        return texto

    def imprimir(self):
        print(f"Veiculo: {self}")
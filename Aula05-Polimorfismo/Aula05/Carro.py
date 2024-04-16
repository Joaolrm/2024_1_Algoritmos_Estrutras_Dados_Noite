from Veiculo import Veiculo 

class Carro(Veiculo):
    def __init__(self, marca, ano, cat, qtdPortas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = qtdPortas

    def __str__(self):
        texto = f"""
        {super().__str__()}
        Portas: {self.qtdPortas}"""
        return texto

    def imprimir(self):
        print(self)
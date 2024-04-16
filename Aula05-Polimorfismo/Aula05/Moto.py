from Veiculo import Veiculo 

class Moto(Veiculo):
    def __init__(self, marca, ano, cat, cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas

    def __str__(self):
        return f"""{super().__str__()}
        Cilindradas: {self.cilindradas}"""

    def imprimir(self):
        print(f"Moto: {self}")
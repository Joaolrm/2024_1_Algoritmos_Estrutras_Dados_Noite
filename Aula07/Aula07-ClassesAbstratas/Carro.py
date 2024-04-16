from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano, nPortas):
        super().__init__(modelo, ano)
        self.qtdPortas = nPortas

    def ligar(self, chave):
        if chave == "1234":
            print("Carro ligado")

        else:
            print("Não foi possivel ligar o carro")

    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de portas: {self.qtdPortas}")
from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        informacoes = f"""{super().getInformacoes()}
        Fonte: {self._potenciaDaFonte}"""
        return informacoes

    def cadastrar(self):
        print(f"""insert:{self.getInformacoes()}""")
from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        informacoes = f"""{super().getInformacoes()}
        Fonte: {self.__tempoDeBateria}"""
        return informacoes

    def cadastrar(self):
        print(f"""insert:{self.getInformacoes()}""")
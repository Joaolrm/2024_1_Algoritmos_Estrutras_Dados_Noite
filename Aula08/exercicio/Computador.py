from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        informacoes = f"""
        Modelo: {self.modelo}
        Cor: {self.cor}
        Preco: {self.preco}"""
        return informacoes

    @abstractmethod
    def cadastrar(self):
        pass
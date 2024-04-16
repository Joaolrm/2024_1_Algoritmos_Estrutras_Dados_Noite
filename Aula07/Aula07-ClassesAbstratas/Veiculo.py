from abc import ABC, abstractmethod

# class Veiculo(metaclass=ABCmeta)
class Veiculo(ABC):
    
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano


    @abstractmethod
    def ligar(self, chave):
        pass

    def imprimir(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    def desligar(self):
        print("Veículo desligado")
from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    
    def __init__(self, nome, numConta, cpf, saldo):
        self.nome = nome
        self.numConta = numConta
        self.cpf = cpf
        self.saldo = saldo


    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass




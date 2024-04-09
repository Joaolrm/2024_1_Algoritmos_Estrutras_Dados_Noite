from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = str(cpf)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCPF(self):
        print (self.__cpf)
        return self.__cpf

    def __calculaIMC(self, peso, altura):
        imc = peso/altura**2
        return imc
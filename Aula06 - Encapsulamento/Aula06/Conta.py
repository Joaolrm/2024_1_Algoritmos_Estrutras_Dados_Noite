class Conta:

    tarifa = 1.99
    logado = True

    def __init__(self):
        self.__saldo = 0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Ação não permitida")
            return None

    def setSaldo(self, valor):
        if self.logado and valor >= 0:
            self.__saldo = valor
        
        else:
            print("Ação não permitda")

    @property
    def saldo(self):

        if self.logado:
            return self.__saldo
        else:
            print("Ação não permitida")
            return None  

    @saldo.setter
    def saldo(self, valor):
        if self.logado and valor >= 0:
            self.__saldo = valor
            
        else:
            print("Ação não permitida")

    def __descontarTarifa(self):
        self.__saldo -= self.tarifa

    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa()

        else:
            print("Saldo insuficiente!")

    def sacar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()

        else:
            print("Saldo insuficiente!")

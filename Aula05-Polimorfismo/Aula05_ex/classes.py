class Veiculo():
    def __init__(self, marca, qtdRodas, modelo):
        self.marca = str(marca)
        self.qtdRodas = int(qtdRodas)
        self.modelo = str(modelo)
        self.velocidade = int(0)

    def __str__(self):
        return f"""Marca: {self.marca}
        Quantidade de rodas: {self.qtdRodas}
        Modelo: {self.modelo}
        Velocidade: {self.velocidade}"""

    def imprimirInformacoes(self):
        print(self)

    def acelerar(self, velocidade):
        self.velocidade += velocidade

    def frear(self, velocidade):
        self.velocidade -= velocidade



class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
        super().__init__(marca, qtdRodas, modelo)
        self.numMarchas = int(numMarchas)
        self.bagageiro = bool(bagageiro)

    def __str__(self):
        return super().__str__() + f"""
        Numero de marchas: {self.numMarchas}
        Bagageiro: {self.bagageiro}"""

    def imprimirInformacoes(self):
        print(self)



class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def __str__(self):
        return super().__str__() + f"""
        Potencia do motor: {self.potenciaDoMotor}"""

    def imprimirInformacoes(self):
        print(self)


class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor)
        self.partidaEletrica = bool(partidaEletrica)


    def __str__(self):
        return super().__str__() + f"""
        Partida eletrica: {self.partidaEletrica}"""

    def imprimirInformacoes(self):
        print(self)


class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor)
        self.qtdPortas = int(qtdPortas)


    def __str__(self):
        return super().__str__() + f"""
        Quantidade de portas: {self.qtdPortas}"""

    def imprimirInformacoes(self):
        print(self)
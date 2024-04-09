from Pessoa import Pessoa
class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEsadual, quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = str(cnpj)
        self.__inscricaoEsadual = str(inscricaoEsadual)
        self.quantidadeFuncionarios = int(quantidadeFuncionarios)

    def imprimeCNPJ(self):
        print (self.__cnpj)


    def __emitiraNotaFicas(self, peso, altura):
        print("Nota fiscal emitida")

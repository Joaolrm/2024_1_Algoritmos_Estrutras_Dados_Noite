from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, nome, numConta, cpf, saldo):
        super().__init__(nome, numConta, cpf, saldo)

    def cadastrar(self):
        cadastro = f"""
            nome: {self.nome}
            numConta: cc{self.numConta}
            cpf: {self.cpf}
            saldo: {self.saldo}
        """
        
        return cadastro

    def depositar(self, valor):
        self.saldo += valor

        


    
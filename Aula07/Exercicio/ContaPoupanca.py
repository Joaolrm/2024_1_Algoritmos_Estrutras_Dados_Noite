from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome, numConta, cpf, saldo, saldocp):
        super().__init__(nome, numConta, cpf, saldo)
        self.saldocp = saldocp

    def cadastrar(self):
        cadastro = f"""
            nome: {self.nome}
            numConta: cp{self.numConta}
            cpf: {self.cpf}
            saldo: {self.saldo}
            saldocp: {self.saldocp}
        """
        
        return cadastro

    def depositar(self, valor):
        poup = input(f"Depositar na poupança?")
        if poup == "S":
            self.saldocp += valor
        else:
            self.saldo += valor

    
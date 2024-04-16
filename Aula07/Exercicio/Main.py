from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

cc = ContaCorrente("João", 1234, 66666666666, 0)
cp = ContaPoupanca("Maria", 4321, 77777777777, 0, 0)

print( cc.cadastrar() )
print( cp.cadastrar() )

cc.depositar(150)
cp.depositar(150)

print( cc.cadastrar() )
print( cp.cadastrar() )
from Carro import Carro
from Moto import Moto

c = Carro("Doblo", 2005, 4)
c.ligar(chave='1234')
c.imprimir()
c.desligar()

print("--------------------------")

m = Moto("CG", 2024, 160)
m.ligar(chave='1234')
m.imprimir()
m.desligar()

from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Categoria import Categoria
from Pedido import Pedido


c1 = Cidade(1)
c2 = Cidade(nome="Porto Alegre")
c3 = Cidade( 1, "Capão da Canoa")

print(c1)
c1.nome = "POA"
print(c1)

print(c2)
print(c3)

p1 = Pessoa("João")
p2 = Pessoa("Maria", 20)
p3 = Pessoa("José", 25, c1)
p4 = Pessoa("José", cid = c2)
p5 = Pessoa("Júlia", idade = 30)

# print(p4.idade)

print("-------Tirar Pedido-------")

cat01 = Categoria( None, "Bebidas")

prod01 = Produto("Coca-Cola", 7.99, 100, cat01)
prod02 = Produto("Pespi", 5.99, cat = cat01)
prod03 = Produto("Amendoin")

ped01 = Pedido("Rua A, 100", p1)
print(ped01)

total = ped01.addproduto(prod01)
print(f"            Total do Pedido {str(total)}")

total = ped01.addproduto(prod02)
print(f"Total do Pedido {str(total)}")
print(f"Total do Pedido {str(ped01.addproduto(prod03))}")
print(ped01)
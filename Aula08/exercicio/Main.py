# Construir código necessário em Python para implementar o seguinte projeto: Uma classe abstrata chamada de Computador que contém os atributos/propriedades: modelo, cor e preço. Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().
 
# O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador. A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. Esta classe reimplementa o método getInformacoes() herdado de computador.
 
# A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o método getInformacoes() herdado de computador.
 
# Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.

from Desktop import Desktop
from Notebook import Notebook

desk1 = Desktop("ThinkCentre", "Preto", 2300.00, "500W")
print (f"Print do get: {desk1.getInformacoes()}")
print()
desk1.cadastrar()
print()
note1 = Desktop("Lenovo", "Cinza", 2400.00, "4h")
print (f"Print do get: {note1.getInformacoes()}")
print()
note1.cadastrar()
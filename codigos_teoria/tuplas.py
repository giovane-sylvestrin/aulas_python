"""
Tuplas (tuples)

Semelhantes as listas

1) representadas entre ( )
2) são imutáveis: uma nova tupla não pode ser alterada (soma, remoção de elementos - append, pop). Quando se altera cria uma nova tupla
3) é possivel entretanto reescrever uma tupla

"""

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print((type(tupla1)))

tupla2 = 1, 2, 3, 4, 5, 6  # também é a representação de uma tupla
print(tupla2)
print(type(tupla2))

# Uma tupla de um elemento não é uma tupla, é necessário o uso da vírgula (que define uma tupla)
tupla3 = (4)
print(type(tupla3))

tupla4 = (4,)  # é uma tupla
print(type(tupla4))
print(tupla4)

# tupla com range(inicio, fim, passo)
tupla5 = tuple(range(10))
print(tupla5)

# desempacotamento de tupla
tupla6 = ('calculo', 'algebra', 'fisica')
materia1, materia2, materia3 = tupla6

print(materia1)
print(materia2)
print(materia3)
print(tupla6[1])

# métodos para adição, remoção de elementos na tupla não existem -> imutáveis

# soma, valor maximo, valor minimo, tamanho
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

# concateanção de tuplas
tupla7 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla7)

# sobreescrevendo uma tupla, forma de alterar o conteudo de uma tupla
tupla1 = tupla1 + tupla7
print(tupla1)

# verificar se um elemento esta na tupla
print(3 in tupla1)
print(30 in tupla1)

# iterando sobre uma tupla
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

# contar elementos em uma tupla -> count
tupla8 =('a', 'b', 'f', 'a', 'd', 'f')
print(tupla8.count('a'))

univ = tuple('UNILA')
print(univ)
print(univ.count('U'))

# quando usar uma tupla?
# 1) quando não é necessário alterar os dados da coleção. Ex: tupla com meses do ano
# 2) tuplas são mais rapidas (na área de dados)
# 3) deixam o código mais segura (imutabildiade)

# O acesso a elementos de uma tupla é similar ao da lista
print(tupla1[10])

# iterando com while
i = 0
while i < len(tupla2):
    print(tupla2[i])
    i += 1

# verificar indice de um elemento na tupla -> index
print(tupla2.index(1))

# demais comandos rever o arquivo de listas, tudo segue a mesma sintaxe
# em tupla não tem o problema de shallow copy
# dir(tupla)

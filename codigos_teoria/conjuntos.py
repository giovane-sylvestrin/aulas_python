"""
Conjuntos (Sets)- se refere a teoria matemática dos conjuntos

- NÃO possuem valores duplicados
- NÃO possuem ordenação
- Elemntos NÃO são acessados via index

Uso:
- Armazenar elementos sem importancia da ordenação

são referenciados com { }
Sets possuem apenas valor

"""

# definindo conjuntos

s = set({1, 2, 3, 5, 6, 7, 15, 2, 5, 1})  # com elementos repetidos, os elementos repetidos não são considerados
print(s)

s = {1, 2, 3, 5, 6, 7, 15, 2, 5, 1}
print(s)

# verificar a existencia de um item no conjunto

if 3 in s:
    print('tem o valor')
else:
    print('não tem o valor')

# iterar um set

for n in s:
    print(n)

# Uso: transformar uma lista em set para descobrir o numero de itens duplicados

cidades = ['A', 'A', 'B', 'C', 'B']
print(len(cidades))
print(len(set(cidades)))

# Adicionar elementos em um set -> add
s.add(57)
print(s)

# remover elementos
s.remove(57)  # se o valor n existir da erro
print(s)

s.discard(151)  # se o valor n existir não apresenta erro
print(s)

# copiar conjuntos: usa-se o copy (deep copy) e o processo set1 = set (shallow copy) - similar a listas

# remover todos os elementos -> clear

# operações de conjuntos matemáticos

conjA = {'A', 'B', 'C', 'D'}
conjB = {'B', 'C', 'Z', 'H', 'G', 'M'}

# união -> union
conjC = conjA.union(conjB)
print(conjC)

# união com pipe |
conjD = conjA | conjB
print(conjD)

# interseção -> intersection
conjE = conjA.intersection(conjB)
print(conjE)

# interseção com &
conjF = conjA & conjB
print(conjF)

# elementos que não estão contidos em outro conjunto -> difference
conjG = conjA.difference(conjB)
print(conjG)

# soma, valor maximo, valor minimo, tamanho
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

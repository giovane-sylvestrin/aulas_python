"""
Module collections -> Counter
https://docs.python.org/3/library/collections.html

Implementações alternativas às implementaçãoes coleções built-in (listas, tuplas, dicionarios, mapas)
Collections -> high performance container datetypes

Counter: recebe um iterável (lista, tupla, dicionario, string, ...) como parâmetro e cria um objeto do tipo Collections
Counter semelhante a um dicionário, com a chave sendo dada pelo elemento da lista passada como parâmetro, e valor como
a quantidade de ocorrências desse elemento

"""

# utilizando Counte

from collections import Counter  # importando uma biblioteca para a aplicação

lista = [1, 2, 3, 4, 7, 9, 9, 6, 3, 7, 7, 2, 8]

resp = Counter(lista)
print(resp)
print(type(resp))

# Listas as repetições mais comuns -> most_common
print(resp.most_common(5))  # 5 mais comuns

for chave in resp:
    print(f'{chave} = {resp[chave]}')


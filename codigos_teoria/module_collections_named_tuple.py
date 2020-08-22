"""
Module collections -> Named Tuple
https://docs.python.org/3/library/collections.html

Atribui um nome a cada parâmetro de uma tupla

"""

from collections import namedtuple

# declaração

cachorro = namedtuple('cachorro', 'raça nome')  # forma 1

cachorro = namedtuple('cachorro', 'raça, nome')  # forma 2

cachorro = namedtuple('cachorro', ['raça', 'nome'])  # forma 3 (recomendado)

# Uso
ray = cachorro(raça='A', nome='ray')  # cria uma variavel cachorro com dois parâmetros
print(ray)

print(ray[0])
print(ray[1])

print(ray.raça)
print(ray.nome)

# possivel usar todos os comandos de tuplas
print(ray.index('A'))
print(ray.count('A'))
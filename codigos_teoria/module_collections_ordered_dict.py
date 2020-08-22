"""
Module collections -> Ordered Dict
https://docs.python.org/3/library/collections.html

Em um dicionário a ordem de inserção de um elemento não é garantida

"""

from collections import OrderedDict

dicion = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicion.items():
    print(f'{chave} = {valor}')

dic1 = dict({'a': 1, 'b': 2})
dic2 = dict({'b': 2, 'a': 1})

print(dic1 == dic2)  # Em dicionario não importa a ordem -> true

dic1 = OrderedDict(dic1)
dic2 = OrderedDict(dic2)

print(dic1 == dic2)  # false



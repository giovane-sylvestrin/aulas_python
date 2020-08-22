"""
Mapas: conehcidos em python como dicionários
"""
receitas = {'jan': 100, 'fev': 150, 'mar': 300, 'abr': 250}

# iterar
for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f'{chave} = {receitas[chave]}')

# conhecer todas as chaves -> keys
print(receitas.keys())

for chave in receitas.keys():
    print(receitas[chave])

# acessando valores -> values

print(receitas.values())

for valor in receitas.values():
    print(valor)

# desempacotamente de dicionarios -> itens
print(receitas.items())

for chave, valor in receitas.items():
    print(f'{chave} = {valor}')

# soma, valor maximo, valor minimo, tamanho
print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas))

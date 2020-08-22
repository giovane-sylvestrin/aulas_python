"""
Dicionários

são coleções do tipo chave: valor, representados por chaves {}
print(type({})) -> retorna dict
NÃO se pode ter chaves repetidas
"""
# criação de dicionarios 1
paises = {'br': 'Brasil', 'pt': 'Portugal', 'esp': 'Espanha'}  # chave : valor, ambos podem ser de qualquer tipo
print(paises)

# criação de dicionario 2
paises2 = dict(eua='Estados Unidos', fr='França', ing='Inglaterra')
print(paises2)

# Acessar elementos (não são indexáveis): 1) via chaves
print(paises['br'])

# 2) acessar via get (recomendado)
print(paises.get('br'))
print(paises.get('ru'))  # quando n existe correspondencia retorna None (tipo de dado sem nome, vazio, sem tipo)
# None pode ser utilizado para inicializar uma variável

pais = paises.get('pt')

if pais:
    print('Pais encontrado')
else:
    print('Pais n encontrado')

pais = paises.get('ru', 'Nao encontrado')  # se não encontrar o valor da chave informada, atribui outro valor
print(f'Pais status: {pais}')

# verificar se uma chave se encontra no dicionario
print('br' in paises)
print('br' in paises2)

# Pode-se utilizar qualquer tipo de lado
localidade = {
    (10, 10): 'posição 1',
    (7, 9): 'posição 2',
    (3, 2): 'posição 3',
}

print(localidade)

# adicionar elementos em um dicionario
paises['ru'] = 'Russia'
print(paises)

novo_dado = {'uru': 'Uruguai'}
paises.update(novo_dado)
print(paises)

# atualizar dados
paises['uru'] = 'Uruguay'
print(paises)

paises.update({'ru': 'Russian'})
print(paises)

# remover dados de um dicionário
paises.pop('pt')  # se não for encontrado resulta erro no código
print(paises)

del paises['esp']  # se não for encontrado resulta erro no código
print(paises)

# Usando dicionario com lista (poderia ser tupla também)
prd1 = {'nome': 'PS2', 'qtd': 2, 'valor': 500}
prd2 = {'nome': 'PS3', 'qtd': 1, 'valor': 800}
prd3 = {'nome': 'PS4', 'qtd': 3, 'valor': 3500}
prd4 = {'nome': 'PS5', 'qtd': 1, 'valor': 5000}

carrinho = []

carrinho.append(prd1)
carrinho.append(prd2)
carrinho.append(prd3)
carrinho.append(prd4)

print(carrinho)
print(carrinho[2])

# limpar dicionario

d = dict(a=1, b=2, c=3)
print(d)

# limpar dicionário -> clear
d.clear()
print(d)

# copiando -> copy (deep copy)

novo = d.copy()
print(novo)

novo['e'] = 5
print(novo)

# criar dicionario com fromkeys (recebe dois parametros: iterável e valor)

usuario = {}.fromkeys(['nome', 'email', 'idade'], 'descomhecido')  # cada elemento da lista vira uma chave, enquanto que o segundo item é atribuido para todos
print(usuario)

teste = {}.fromkeys('abcde', 1)
print(teste)

teste2 = {}.fromkeys(range(10), 'novo')
print(teste2)




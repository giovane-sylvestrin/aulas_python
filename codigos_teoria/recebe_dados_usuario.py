"""
Recebendo dados do usuário

Todo input() é recebido como uma variável do tipo string
"""
# print("Qual seu nome?")
# nome = input()  # faz a leitura do teclado
nome = input('Qual seu nome? ')

# print versão 2.x
# print('Seja bem vindo(a) %s' % nome)

# print versão 3.x
# print('Seja bem vindo(a) {0}', format(nome))

# Atual
print(f'Seja bem vindo(a) {nome}')

# print('Qual sua idade? ')
# idade = input()
# idade = input('Qual sua idade? ')g
idade = int(input('Qual sua idade? '))

# print('%s tem %s anos' % (nome, idade))
# print('{0} tem {1} anos', format(nome, idade))
print(f'{nome} tem {idade} anos')

# print(f'Você nasceu em {2020 - int(idade)}')

"""
int(idade) é um cast

Conversão de um tipo de dado em outro
"""

print(f'Você nasceu em {2020 - idade}')

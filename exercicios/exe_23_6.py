"""
num = int(input('Insira um numero inteiro: '))
div = ''
j = 0

for i in range(1, num + 1):
    x = num % i
    if x == 0:
        div += f'{i} '
        j += 1

print(f'Os numeros divisores de {num} são: {div}')

MELANIE
print('Escribí un número pedazo de drácula:')

N = int(input())
contador =0

for i in range(1,N+1):
    if N % i == 0:
        contador += 1
        print(f'Divisor #{contador} = {i},', end=' ')
"""
num = int(input('Insira um numero inteiro: '))
div = ''
j = 0

for i in range(1, num + 1):
    x = num % i
    if x == 0:
        div += f'{i} '
        j += 1

print(f'Os numeros divisores de {num} são: {div}')

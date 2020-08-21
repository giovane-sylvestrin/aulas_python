"""
numero = 0
menor = 0
maior = 0

for i in range(1, 5):
    numero = float(input(f'Insira o #{i}: '))
    compara = numero
    if i == 1:
        menor = numero
        maior = numero
    if compara < menor:
        menor = compara
    if compara > maior:
        maior = compara

print(f'Menor numero: {menor}')

print(f'Maior numero: {maior}')
"""
numero = 0
menor = 0
mayor = 0

for n in range(1, 5):
    print(f'Ingresse o valor #{n}:')
    numero = int(input())
    menor = numero
    # mayor = numero
    if numero < menor:
        menor = numero

print(f'El menor valor es {menor}')
"""
num = int(input('Insira um numero: '))

while True:
    if num % 11 == 0:
        print(f'{num} é multiplo de 11')
        break
    if num % 13 == 0:
        print(f'{num} é multiplo de 13')
        break
    if num % 17 == 0:
        print(f'{num} é multiplo de 17')
        break
    num += 1

print('FIM')
"""
print('Ingresse um número:')
N = int(input())

primeiro_apos_11 = N/11
if(primeiro_apos_11-int(primeiro_apos_11) < 0,5):
    primeiro_apos_11_2 = int(primeiro_apos_11)+1
else:
    primeiro_apos_11_2 = int(primeiro_apos_11)

primeiro_apos_13 = int(N/13)
if(primeiro_apos_13-int(primeiro_apos_13) < 0,5):
    primeiro_apos_13_2 = int(primeiro_apos_13)+1
else:
    primeiro_apos_13_2 = int(primeiro_apos_13)

primeiro_apos_17 = int(N/17)
if(primeiro_apos_17-int(primeiro_apos_17) < 0,5):
    primeiro_apos_17_2 = int(primeiro_apos_17)+1
else:
    primeiro_apos_17_2 = int(primeiro_apos_17)


print(f'Posição do primeiro após 11: {primeiro_apos_11_2}, primeiro múltiplo após 11: {primeiro_apos_11_2*11}')
print(f'Posição do primeiro após 13: {primeiro_apos_13_2}, primeiro múltiplo após 13: {primeiro_apos_13_2*13}')
print(f'Posição do primeiro após 17: {primeiro_apos_17_2}, primeiro múltiplo após 17: {primeiro_apos_17_2*17}')



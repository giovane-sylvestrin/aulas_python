"""
import random
num = random.randint(1, 1000)
n = 0

while True:
    chute = int(input('Chute um núemro inteiro de 1 a 1000: '))
    if chute < num:
        print('Seu chute foi abaixo do valor certo, tente de novo')
    if chute > num:
        print('Seu chute foi acima do valor certo, tente de novo')
    if chute == num:
        print(f'MUUUY BIEEN CHEE, mira acertaste em {n} tentativas ')
        break
    n += 1
"""
import random
print('Si no acertas es que te falta una banda, una banda de leche gil.')

gerado = random.randint(1, 10)

while True:

    chutado = int(input('Tente acertar o número cachorro de leche: '))

    if gerado == chutado:
        print(f'O número gerado pelo sistema é {gerado}')
        print(f'Parabens, vc fez um chute cosmico.')
        break
    elif chutado > gerado:
        print(f'O valor {chutado} é maior que o gerado pelo sistema.')
    elif chutado < gerado:
        print(f'O valor {chutado} é menor que o gerado pelo sistema.')



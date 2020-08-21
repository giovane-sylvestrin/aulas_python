"""
Estruturas de repetição

loop
for

nome = 'Giovane Sylvestrin'
lista = [1, 2, 3, 4, 5]
numero = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1, 10):
    print(numero)

for x in range(2, 30, 3):
    print(x)

# uso do enumerate(): para cada elemento do iterável, atribui um indice
# ((0, 'G'), (1, 'i'), (2, 'o'), ...) = ((i, v), ...)

for i, v in enumerate(nome):
    print(nome[i])

for i in enumerate(nome):  # retorna os par (i, v)
    print(i)

for i in enumerate(nome):  # retorna openas o segundo valor do par (i, v)
    print(i[1])

for i, v in enumerate(nome):
    print(v)

for _, v in enumerate(nome):  # _ descarta algo, no caso descarta o indice
    print(v)


qtd = int(input("Numero de repetições "))
soma = 0

for i in range(0, qtd+1):
    print(f'Imprimindo {i}')  # print(f'Imprimindo {i}', end=' ') termina o print com espaço

for i in range(1, qtd + 1):
    num = float(input(f'Soma elemento {i}/{qtd} '))
    soma += num

print(f'Soma total é {soma}')

for i in range(0, 5):
    print(f"{'GIO ' * i}")

# emojis code https://apps.timwhitlock.info/emoji/tables/unicode
# Original U+1F621
# Modificado U0001F621

for i in range(3):
    for j in range(1, 4):
        print('\U0001F621' * j)
****************************************************************************

Ranges

range(valor da parada) -> o valor não esta incluso na sequencia
                          inicio em 0 até o valor, de 1 em 1

range(valor inicial, valor final)

range(valor inicial, valor final, passo)

range(valor inicial, valor final, -passo) -> para contagem regressiva

converter range em lista

lista = list(range(10)) -> retorna [0, 1, 2, ..., 9]

*****************************************************************************

while

num = 0

while num <=10:
    print(num)
    num +=1

resposta = ''

while resposta != 'sim':
    resposta = input(f'Voce entendeu?: ')

**********************************************************************

break

"""

for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)

print("Fora do loop")

while True:
    comando = input(f"insira sair: ")
    if comando == 'sair':
        break

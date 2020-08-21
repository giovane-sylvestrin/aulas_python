"""
n = int(input('Insira um número estilo proprio bo: '))
num = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        num += 1
        print(num, end=' ')
    print(' ')
"""
n = int(input('Insira um número estilo proprio bo: '))
i = 1
j = 1
contador = 1

while True:
    if contador > n:
        break
    lista = list(range(i, j+1))
    print(lista)
    i = j + 1
    contador += 1
    j += contador

n = int(input('Linhas do Triangulo de Floyd:'))
contador = 0

for i in range(0, n):
    lst = []
    for n in range(0,i+1):
        contador += 1
        lst.append(contador)
    print(lst)

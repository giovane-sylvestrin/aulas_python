"""
import time
ini = time.time()
primo = 0
intervalo = 2000
soma = 0

for i in range(1, intervalo):
    div = 0
    for j in range(1, i+1):
        if i % j == 0:
            div += 1
            if div > 2:
                break
    if div == 2:
        primo += 1
        soma += i

print(f'Existem {primo} números primos no intervalo menor que {intervalo}, a soma dos números é de {soma}')
fim = time.time()
print(f'Tempo de execução {round(fim-ini, 5)}s')
"""

import time
ini = time.time()
soma = 2
resta=0

for i in range(3, 2000):
    soma += i
    for n in range(2,i):
        comparador = i % n
        if comparador == 0:
            resta -= i
            break
print(soma+resta)
fim = time.time()
print(f'Tempo de execução {round(fim-ini, 5)}s')

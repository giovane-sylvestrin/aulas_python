"""
n = int(input('Insira o numero de termos da série: '))
numer = 0
denom = 1
s = 0

for i in range(1, n):
    numer = i
    n = 2*i
    denom = 1
    for j in range(n, 0, -1):
        denom *= j
    s += numer/denom

print(f'O valor da série é {s}')

"""
n = int(input('Insira um numero: '))
denominador = 1
nominador = 0
H_n = 0



for i in range(1, 2*n + 1):
    denominador = 1

    if i % 2 == 0:
       nominador += 1
       print(f'nominador: {nominador}')
       for f in range(i, 0, -1):
            denominador *= f
       print(f'denominador: {denominador}')
       H_n += nominador/denominador
       print(f'H_n = {H_n}')



print(f'H_n {H_n}')

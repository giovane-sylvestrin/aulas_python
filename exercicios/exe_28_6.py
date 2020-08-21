"""
import math
num = int(input('Insira um numero: '))
e = 0

if num < 0:
    num = int(input('Insira um numero válido (inteiro positivo): '))

for i in range(0, num + 1):
    if i == 0:
        e = 1
    else:
        e += 1/math.factorial(i)

print(f'O valor de E é {e}')
"""
from fractions import Fraction
n = int(input('Insira um numero: '))
denominador = 1
H_n = 1

for i in range(1, n+1):
    denominador = 1
    for f in range(i, 0, -1):
        denominador *= f
    H_n += 1/denominador

fraccion = Fraction(str(H_n)).limit_denominator()

print(f'H(n) = {fraccion} = {H_n}')

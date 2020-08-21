from fractions import Fraction

n = int(input('Insira um numero: '))
n_i = 0
H_n = 0

for i in range(1,n+1):
    H_n += 1/i

fraccion = Fraction(str(H_n)).limit_denominator()

print(fraccion)

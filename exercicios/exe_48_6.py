"""
an = 1
a_ant = 1
a_antt = 0
soma_par = 0

while True:
    an = a_ant + a_antt
    a_antt = a_ant
    a_ant = an
    if an % 2 == 0 and an < 4e06:
        soma_par += an
    if an > 4e06:
        break

print(soma_par)
"""
n1 = 1
n2 = 1
soma = 0
while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    #print(n3)
    if n3 % 2 == 0:
        soma += n3
    if n3 > 4_000_000:
        break
print(f'A soma é: {soma}')

num = input('Insira um número inteiro entre 100 e 999: ')
soma = 0
elem = list(num)

for i in elem:
    soma += int(i)
    print(i)

print(soma)

num = 0
i = 0
j = 0

while True:
    num = int(input("Insira um núemro: "))
    if num == 1000:
        break
    if num % 2 == 0:
        print(f'{num} é par')
        i += 1
    else:
        print(f'{num} é impar')
        j += 1

print(f'Foram lidos {i + j} numeros, com {i} par(es) e {j} impa(res)')

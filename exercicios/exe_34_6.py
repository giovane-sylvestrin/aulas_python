inf = int(input("insira o intervalo inferior: "))
sup = int(input("Insira o intervalo superior: "))
j = sup
cont = 0
menor_div = 0

while True:
    cont = 0
    for i in range(inf, sup + 1):
        if j % i == 0:
            cont += 1
    if cont == (sup - inf) + 1:
        menor_div = j
        break
    j += 1
    if j > 1000000:
        break


print(f'O menor numero divisivel no intervalo de {inf} a {sup} é de {menor_div}')

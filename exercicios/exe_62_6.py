
um = 2
dois = 4
tres = 4
quatro = 6
cinco = 5
seis = 4
sete = 4
oito = 4
nove = 4
zero = 4

soma_1 = um + dois + tres + quatro + cinco + seis + sete + oito + nove + zero
soma_2 = 0
soma_3 = 0
soma_4 = 14

lst = range(1001)

for i in range(10,100):

    primer_casa = lst[i] % 10

    if primer_casa == 1:
        primer_casa = 2
    elif primer_casa == 2 or primer_casa == 3 or primer_casa == 6 or primer_casa == 7 or primer_casa == 8 or primer_casa == 9 or primer_casa == 0:
        primer_casa = 4
    elif primer_casa == 4:
        primer_casa = 6
    elif primer_casa == 5:
        primer_casa = 5

    segunda_casa = lst[i] // 10

    if segunda_casa == 1:
        segunda_casa = 2
    elif segunda_casa == 2 or segunda_casa == 3 or segunda_casa == 6 or segunda_casa == 7 or segunda_casa == 8 or segunda_casa == 9 or segunda_casa == 0:
        primer_casa = 4
    elif segunda_casa == 4:
        segunda_casa = 6
    elif segunda_casa == 5:
        segunda_casa = 5

    numero = primer_casa + segunda_casa
    soma_2 += numero

for i in range(100,1000):

    segunda_primera = lst[i] % 100

    primer_casa_2 = segunda_primera % 10

    if primer_casa_2 == 1:
        primer_casa_2 = 2
    elif primer_casa_2 == 2 or primer_casa_2 == 3 or primer_casa_2 == 6 or primer_casa_2 == 7 or primer_casa_2 == 8 or primer_casa_2 == 9 or primer_casa_2 == 0:
        primer_casa_2 = 4
    elif primer_casa_2 == 4:
        primer_casa_2 = 6
    elif primer_casa_2 == 5:
        primer_casa_2 = 5

    segunda_casa_2 = segunda_primera // 10

    if segunda_casa_2 == 1:
        segunda_casa_2 = 2
    elif segunda_casa_2 == 2 or segunda_casa_2 == 3 or segunda_casa_2 == 6 or segunda_casa_2 == 7 or segunda_casa_2 == 8 or segunda_casa_2 == 9 or segunda_casa_2 == 0:
        primer_casa_2 = 4
    elif segunda_casa_2 == 4:
        segunda_casa_2 = 6
    elif segunda_casa_2 == 5:
        segunda_casa_2 = 5

    tercer_casa = lst[i] // 100

    if tercer_casa == 1:
        tercer_casa = 2
    elif tercer_casa == 2 or tercer_casa == 3 or tercer_casa == 6 or tercer_casa == 7 or tercer_casa == 8 or tercer_casa == 9 or tercer_casa == 0:
        tercer_casa = 4
    elif tercer_casa == 4:
        tercer_casa = 6
    elif tercer_casa == 5:
        tercer_casa = 5

    numero_2 = primer_casa_2 + segunda_casa_2 + tercer_casa
    soma_3 += numero_2


print(f'Soma 0 - 9: {soma_1}')
print(f'Soma 10 - 99: {soma_2}')
print(f'Soma 100 - 1000: {soma_3 + soma_4}')
print(f'Soma total 0 - 1000: {soma_1 + soma_2 + soma_3 + soma_4}')


lista = str(list(range(0, 1001)))
i = 0
soma = 0

while True:
    if lista[i] == '0' or lista[i] == '2' or lista[i] == '3' or lista[i] == '6' or lista[i] == '7' or lista[i] == '8' or lista[i] == '9':
        soma += 4
    elif lista[i] == '1':
        soma += 2
    elif lista[i] == '4':
        soma += 6
    elif lista[i] == '5':
        soma += 5
    elif lista[i] == ']':
        break
    else:
        soma += 0
    i += 1

print(soma)

print(lista[i-1])
print(lista[i-2])
print(lista[i-3])
print(lista[i-4])
print('fim')
#lista = str(list(range(10, 100)))


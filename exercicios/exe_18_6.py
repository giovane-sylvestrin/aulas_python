qtd = int(input(f'Qual a quantidade de numeros a serem lidos? '))
maior = 0
cont = 0

for i in range (1, qtd + 1):
    num = float(input(f'Insira o #{i}: '))
    if i == 1:
        maior = num
    if num >= maior:
        if num > maior:
            cont = 0
        maior = num
        cont += 1
print(f'O maior numero inserido foi {maior}, repetido {cont} vez(es)')

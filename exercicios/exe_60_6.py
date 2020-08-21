soma = 0
soma_par = 0
cont = 0
cont_par = 0

while True:
    num = int(input('Insira um número inteiro (zero para parar): '))
    if num == 0:
        break
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        soma_par += num
        cont_par += 1

print(f'\nForam inseridos {cont} números \nQue somados resultam em {soma} \nCom média de {round(soma/cont, 2)} \nMaior numero foi {maior}, e o menor foi {menor} \nMédia dos pares foi de {round(soma_par/cont_par, 2)}')

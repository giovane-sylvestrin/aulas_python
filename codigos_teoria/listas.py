"""
Listas: vetores ou matrizes, dinamicas, qualquer tipo de dado

"""
num = 15
lista1 = list(range(11))

# Identificar elementos presentes

if num in lista1:
    print(f'Valor {num} encontrado')
else:
    print(f'Valor {num} não encontrado')

# Usando a propriedade sort: ordernar
lista2 = [10, 10, 5, 88, 5, 2, 9, 1]
l = ['z', 'd', 'a']
lista2.sort()
print(lista2)
l.sort()
print(l)

# Contagem de ocorrências - count
print(lista2.count(7))

# Adicionar elemento - append

lista2.append(42)
print(lista2)
lista2.append([7, 9, 6])  # adicionar uma lista como elemento, para localizar esse elemento colocar x[i][j], com j o indice da sublista
print(lista2)

# Adicionar elemento - extend

lista2.extend([10, 11, 12])  # adicionar cada item como um elemento, não aceita elemento unico extend(10)
print(lista2)

# Adicionar elemento em posição desejada - insert
lista2.insert(0, 'Novo')
print(lista2)

# Unir listas
lista3 = lista1 + lista2
print(lista3)
# lista1.extend(lista2)
# print(lista1)

# Inverter lista - reverse
lista1.reverse()
print(lista1)
lista1 = lista1[::-1]
print(lista1)

# Copiar uma lista - copy
lista4 = lista1.copy()
print(lista4)

# Verificar tamanho da lista - len
print(len(lista4))

# Remover ultimo elemento de uma lista - pop
lista4.pop()
print(lista4)
lista4.pop(2)
print(lista4)

# Limpar lista - clear
lista4.clear()
print(lista4)

# repetir elementos de uma lista
nova = [1, 2, 3]*3  #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print(nova)

# converter string em lista -> split
frase = 'iiiiisso isso'
frase = list(frase)  # aqui cada elemento vira um componente da lista
print(frase)
frase = "isso isso"  # aqui cada palavra vira um elemento da lista, por padrão split separa por espaço
                     #split('separador')
frase = frase.split()
print(frase)

# converter lista em string -> join(nome da lista)
lista5 = ['iiiisso', 'henry', 'raul']
eliot = ' '.join(lista5)  # separa cada item da lista por espaços
print(eliot)

# iterando sobre listas
soma = 0  # poderia ser uma string vazia ' '
for elemento in lista1:  #imprimi cada elemento da lista
    print(elemento)
    soma = soma + elemento
print(soma)

# indexar lista de forma inversa lista1[-1] acessa o ultimo elemento e assim por diante
print(lista1)
print(lista1[-1])

# gerar indice em uma lista
cores = ['vermelho', 'azul', 'branco', 'amarelo']

for indice, cores in enumerate(cores):
    print(indice, cores)

# encontrar o indice de um elemento de uma lista -> index(elemento)
numeros = [0, 5, 7, 9, 2, 6, 3]
print(numeros.index(7))  # caso existam elementos repetidos, retorna o index do primeiro

# encontrar um indice de um elemento a partir de uma posição desejada
print(numeros.index(9, 2)) # para definir um range .index(valor, inicio, fim)

# slicing -> lista[inicio:fim:passo]
print(lista1[1:])  # inicia no indice um e vai até o fim
print(lista1[1:5])  # inicia no indice um e vai até o 5
print(lista1[1:5:2])  # define um passo

# inverter valores em uma lista -> reverse
nomes = ['giovane', 'melanie']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)

# soma, valor máximo, valor minimo, tamanho (Apenas listas com numeros inteiros ou reais
print(sum(lista1))
print(min(lista1))
print(max(lista1))
print(len(lista1))

# transformar lista em tupla -> tuple
tupla = tuple(lista1)
print(tupla)
print(type(tupla))

# desempacotamento de lista
lista7 = [7, 9, 6]
num1, num2, num3 = lista7  # tem q ter o msm tamanho
print(num1)
print(num2)
print(num3)

# shallow copy -> alteração de uma lista altera a outra
# usar copy não produz isso -> Deep copy
new1 = [1, 2, 3]
new2 = new1

new2.append(4)

print(new1)
print(new2)

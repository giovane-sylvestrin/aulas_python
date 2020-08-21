"""
Variáveis e tipos de dados

***********************************************************
Tipo numérico int

5/2 retorna 2.5
int(5/2) retorna 2
5//2 retorna 2
5%2 retorna 1 (resto)
3**3 retorno 27 (3^3)

ctrl + l limpa o terminal/console

permite separar as milhares com _
Ex: 1_000_000 retorno 1000000

num += 1 (num recebe num +1 , num = num + 1)
num -= 1 (num = num - 1)
num *= 2 (num = num*2)
num /= 2 (num = num/2)

FUNÇÃO type -> retorno o tipo de dado
type(num)
**********************************************************

Tipo float (ponto flutuonte)

x, y = 2.5, 3.77 (x=2.5 y=3.77

float para int
z = int(x) (retorna 2)

5j (numero tipo complexo)
{
x, y = 2.5, 3.77

print(x)
print(y)

z = int(x)
print(z)
}

***********************************************************

Tipo Booleano

verdadeiro ou falso

True
False (sempre em maiúsculo)

Operações básicas

- Negação (not)
    se o boolenao for vdd a negação retorna falso e vice versa
- Ou (or)
    é uma operação binária, depende de dois valores, ou um ou outro deve ser vdd
    True or True -> retorna True
    True or False -> retorna True
    False or Flase -> retorna False
- E (and)
    operação binária onde ambos os valores devem ser vdd para retornar vdd
    True or True -> retorna True
    True or False -> retorna False
    False or Flase -> retorna False

5 < 6 -> retorna True
5 > 6 -> retorna False
5 >= 6 -> retorna False
5 == 5 -> retorna True
{
ativo = False

print(ativo)

print(not ativo)

logado = True

print(ativo or logado)

print(ativo and logado)

num1 = 5
num2 = 8

print(num1 > num2 or num1 >= num2 or num1 < 3)
}

********************************************************

Tipo string

comando \n pula linha
{
nome = 'Giovane'
print(nome)
print(type(nome))

nome2 = 'Giovane \nSylvestrin'
print(nome2)
print(type(nome2))

print(nome.upper())  # Maiuscula
print(nome.lower())  # Minúscula
print(nome2.split())  # transforma em uma lista de strings

# ['G', 'i', 'o', 'v', 'a', 'n', 'e', ' ', 'S', 'y', 'l']
# [0     1    2    3    4    5    6    7    8    9    10]
print(nome2[0:10])  # selecionar os componentes da string -> Slice de string
print(nome2.split()[0])  # seleciona o primeiro elemento da lista criada
print(nome[::-1])  # [::-1] começa do primeira ao ultimo elemento e inverta a ordem
print(nome.replace('G', 'D'))  # substituir elemento

}

***********************************************************

Escopo de variáveis

1 - variáveis globais: escopo (reconhecidas) em todo o programa

2 - variáveis locais: escopo limitado ao bloco onde foi declarada

Python é uma linguagem de tipagem dinâmica, ao declarar uma variavel não
atribuimos um tipo de dado a ela, essa atribuição é inferida quando ele obtem um valor
"""
numero = 50
# novo = 0 declarado aqui passaria a ser uma variável global

if numero > 10:
    novo = numero + 50
    print(novo)

print(novo)

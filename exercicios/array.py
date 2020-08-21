"""
j = 0
cont = [0, 1, 2, 3]

for i in range(4):
    cont[i] = i

print(cont)
"""

arquivo = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r+")
x = arquivo.readlines()
arquivo.close()

length = list(range(len(x)))
print(f'aqui {length}')
i = 0

arquivo = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r+")
for linha in arquivo:
    print(linha)
    length[i] = len(linha)
    i += 1
print(length)

arquivo.close()

teste = []

for i in range(10):
    teste.append(i)

print(teste)

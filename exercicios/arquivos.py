"""
### 16) Escreva um programa ``reverse.py`` para imprimir linhas de um arquivo na ordem inversa.


      $ cat she.txt
      She sells seashells on the seashore;
      The shells that she sells are seashells I'm sure.
      So if she sells seashells on the seashore,
      I'm sure that the shells are seashore shells.

      $ python reverse.py she.txt
      I'm sure that the shells are seashore shells.
      So if she sells seashells on the seashore,
      The shells that she sells are seashells I'm sure.
      She sells seashells on the seashore;
"""

file = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r")
x = file.readlines()
file.close()

print(x)

x.reverse()

for i in x:
    print(i, end="")

file = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r")
lista = file.readlines()
file.close()

y = len(lista)
print(y)


for i in lista:

    y -= 1

    index=lista[y]
    print(index)

"""
da errado

for i in range(len(x), 0, -1):
    print(x[i])
    
print(len(x))

print(type(x))
"""


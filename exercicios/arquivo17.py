"""
17) Escreva um programa `wrap.py` que recebe o nome de um arquivo e um comprimento, e quebra as linhas com comprimento maior que o argumento.


    $ python wrap.py she.txt 30
    I'm sure that the shells are s
    eashore shells.
    So if she sells seashells on t
    he seashore,
    The shells that she sells are
    seashells I'm sure.
    She sells seashells on the sea
    shore;

"""
# seek(offset,from_what)
# offset=number of bytes to be moved
# from_what=specifies the reference position from where the bytes are to be moved

comprimento = 30

arquivo = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r+")
y = arquivo.readlines()
x = list(range(len(y)))

arquivo.seek(0, 0)
j = 0
i = 0

for linha in arquivo:
    x[i] = len(linha)
    print(x[i])
    i += 1

arquivo.seek(0, 0)
for i in range(4):
    j += 1
    print(f'1pt {arquivo.read(comprimento)}')
    print(f'2pt {arquivo.read(x[j-1]-comprimento)}')

arquivo.close()

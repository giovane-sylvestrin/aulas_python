# seek(offset,from_what)
# offset=number of bytes to be moved
# from_what=specifies the reference position from where the bytes are to be moved

comprimento = 20
nome_arquivo = 'ex_17.txt'

#arquivo = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r+")
#x = arquivo.readlines()
arquivo = open("C:/Users/Ultrabook/Documents/Python Curso/she.txt", "r+")
cursor = 0

for linha in arquivo:

    length = len(linha)
    cursor += length
    print(length)

    if len(linha) < comprimento:
        posicion = cursor - length
        arquivo.seek(posicion, 0)
        arquivo.read(length)

    elif len(linha) > comprimento:

        posicion1 = cursor - length
        arquivo.seek(posicion1, 0)
        comprimento1 = comprimento
        arquivo.read(comprimento1)

        posicion2 = cursor - comprimento
        arquivo.seek(posicion2, 0)
        comprimento2 = length - comprimento
        arquivo.read(comprimento2)

arquivo.close()
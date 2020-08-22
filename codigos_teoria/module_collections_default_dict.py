"""
Module collections -> Default Dict
https://docs.python.org/3/library/collections.html

Em dicionario se tentar acessar um valor de uma chave que não existe, há um retorno de erro
dicion['chave n existente'] -> erro

Quando se cria um dicionário com Default Dict, se informa um valor default (pode ser lambda). Este valor é retornado
sempre que não houver uma valor correspondete a uma chave inexistente. Caso se tente acessar a chave, ela é criada e
atribuida com a valor default.

lambdas = são funções sem nome, que podem ou não receber valores de entrada e retornar valores

"""

from collections import defaultdict

dicion = defaultdict(lambda: 0)
print(dicion)

dicion['curso'] = 'Calculo'
print(dicion)

print(dicion['curso2'])  # vai atribuir o valor default 0 a chave curso2
print(dicion)






"""
Estruturas lógicas

and, or, not, is (not é operador unário, is é usado para comparação)

not retorna uma negação, inverte
1 is 1 -> retorna True
1 is 5 -> retorna False

"""
ativo = False
logado = True

if ativo and logado:
    print("Usuário presente")
else:
    print("Usuário ausente")

if ativo or logado:
    print("Usuário ativo ou logado")
else:
    print("Usuário ausente")

if not ativo:
    print("Ative seu usuário")
else:
    print("Conta ativada")

print(logado is True)

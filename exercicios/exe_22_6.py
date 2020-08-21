soma = 0
i = 0

while True:
    nota = float(input('Insira sua nota: '))
    if nota < 10 or nota > 20:
        print('Nota invalida')
        break
    soma += nota
    i += 1

print(f'Sua media foi de: {soma/i}')

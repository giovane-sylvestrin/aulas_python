b = float(input("Insira a medida da base do triângulo pedação de drácula: "))

while True:
    if b <= 0:
        print('Medida invalida pedaço de drácula')
        b = float(input("Insira a medida da base do triângulo pedação de drácula: "))
    if b > 0:
        break

h = float(input("Insira a medida da altura do triângulo pedação de drácula: "))

while True:
    if h <= 0:
        print('Medida invalida pedaço de drácula')
        h = float(input("Insira a medida da altura do triângulo pedação de drácula: "))
    if h > 0:
        break

print(f'A área do triângulo é {(b*h)*2}')

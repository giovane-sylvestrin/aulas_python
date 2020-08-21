"""
Estruturas condicionais

if, else, elif

"""

idade = float(input("Qual a sua idade? "))

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

if idade < 18:
    print("Menor de idade")
    if 12 < idade <= 15:
        print("Adolescente")
    if idade <= 12:
        print("Criança")
else:
    print("Maior de idade")

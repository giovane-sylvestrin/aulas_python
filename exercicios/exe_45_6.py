"""
v_kh = 0
v_ms = 0


while True:
    print("Escolha uma das opções: \n1 - km/h para m/s \n2 - m/s para km/h \n3 - Sair")
    option = int(input())
    if option != 1 and option != 2 and option != 3:
        print('Opção inválida\n')
    if option == 1:
        v_kh = float(input('Velocidade em km/h: '))
        print(f'A velocidade de {v_kh} km/h equivale a {v_kh/3.6} m/s\n')
    if option == 2:
        v_ms = float(input('Velocidade em m/s: '))
        print(f'A velocidade de {v_ms} m/s equivale a {v_ms*3.6} km/h\n')
    if option == 3:
        print('Saindo do programa')
        break

"""
print("Escriba '1' si desea convertir de km/h para m/s.")
print("Escriba '2' si desea convertir de m/s para km/h.")
print("Escriba '3' si desea finalizar.")

while True:
    opcion = int(input("Cachorro de leche, elija la opción: "))
    if opcion == 1:
            velociad_kmh = float(input('Ingrese la velocidad en km/h: '))
            velocidad_ms = velociad_kmh * (1000/3600)
            print(f'Velocidad en m/s = {velocidad_ms}')
    if opcion == 2:
            velocidad_ms = float(input('Ingrese la velocidad en m/s: '))
            velocidad_kmh = velocidad_ms * (3600 / 1000)
            print(f'Velocidad en km/h = {velocidad_kmh}')
    if opcion == 3:
            break

from math import pi


def menu_circulo():
    while True:
        menu = int(
            input(
                "Menu de circulo, 1:Area, 2:Perimetro, 3: Diametro, 4: Esfera, 5: Salir "
            )
        )
        radio = int(input("Ingrese el radio de su circulo "))

        if menu == 1:
            area = radio * pi**2
            print(f"El area de su circulo es: {area:.2f}")

        elif menu == 2:
            perimetro = radio * 2 * pi
            print(f"El perimetro de su circulo es: {perimetro:.2f}")

        elif menu == 3:
            diametro = radio * 2
            print(f"El diametro de su circulo es: {diametro:.2f}")

        elif menu == 4:
            esfera = 4 / 3 * pi * radio**3
            print(f"El volumen de su esfera es: {esfera:.2f}")

        elif menu == 5:
            print("Adios")
            break

        else:
            print("Opcion no valida")

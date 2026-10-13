from math import pi


def suma(dato1, dato2, dato3):
    resultado = dato1 + dato2 + dato3
    print(f"La suma de los 3 numeros es: {resultado}")


def saludar():
    print("Hola")


def calificacion():
    calificacion = int(input("Ingrese la calificacion del examen (0-100): "))
    if calificacion < 60:
        letra = "F"
    elif calificacion < 70:
        letra = "D"
    elif calificacion < 80:
        letra = "C"
    elif calificacion < 90:
        letra = "B"
    else:
        letra = "A"
    print(f"Con {calificacion} tu calificacion es: {letra}")


def visita(nom):
    contador = 0
    contador += 1
    print(f"Hola {nom}, esta es tu visita número {contador}")


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


def numero_negativo():
    numero = 0
    while numero >= 0:
        numero = int(input("Ingrese un numero: "))
    print(f"Ingresaste {numero}, que es negativo. Fin del programa.")


def numeros_primos():
    print("Los numeros primos entre 1 y 100 son:")
    for num in range(2, 101):
        es_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)


def promedio_estudiantes():
    promedio_individual = 0.0
    promedio_global = 0.0
    for i in range(10):
        promedio_individual = 0.0
        for j in range(3):
            nota = float(
                input(
                    f"Ingrese la nota {j + 1} del estudiante {i + 1} en el rango de 1 al 10: "
                )
            )
            promedio_individual = promedio_individual + nota
        promedio_individual = promedio_individual / 3
        print(f"El promedio del estudiante {i + 1} es: {promedio_individual:.2f}")
        promedio_global = promedio_global + promedio_individual
    promedio_individual = 0
    print(f"El promedio global es: {promedio_global / 10:.2f}")


def tabla_multiplicar(num):
    for i in range(1, 11):
        resultado = num * i
        if resultado % 2 == 0:
            print(f"{num} x {i} = {resultado} -> Par")
        else:
            print(f"{num} x {i} = {resultado} -> Impar")


def checar_numero():
    num = int(input("Ingrese un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
        return False

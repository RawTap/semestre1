from math import pi


# funcion para sumar 3 numeros y mostrar el resultado
def suma(dato1, dato2, dato3):
    resultado = dato1 + dato2 + dato3
    print(f"La suma de los 3 numeros es: {resultado}")


# funcion para saludar al usuario
def saludar():
    print("Hola")


# funcion para calcular la calificacion de un examen y mostrarla en letra
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


# funcion para saludar a un usuario y decirle cuantas veces ha visitado el programa
def visita(nom):
    contador = 0
    contador += 1
    print(f"Hola {nom}, esta es tu visita número {contador}")


# funcion para mostrar el menu de circulo y calcular area, perimetro, diametro y volumen de una esfera
def menu_circulo():
    while True:
        menu = int(
            input(
                "Menu de circulo, 1:Area, 2:Perimetro, 3: Diametro, 4: Esfera, 5: Salir "
            )
        )

        if menu == 5:
            print("Adios")
            break

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

        else:
            print("Opcion no valida")


# funcion para checar si un numero es negativo
def numero_negativo():
    numero = 0
    while numero >= 0:
        numero = int(input("Ingrese un numero: "))
    print(f"Ingresaste {numero}, que es negativo. Fin del programa.")


# funcion para mostrar los numeros primos entre 1 y 100
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


# funcion para calcular el promedio de 10 estudiantes, cada uno con 3 notas
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


# funcion para mostrar la tabla de multiplicar de un numero y decir si el resultado es par o impar
def tabla_multiplicar(num):
    for i in range(1, 11):
        resultado = num * i
        if resultado % 2 == 0:
            print(f"{num} x {i} = {resultado} -> Par")
        else:
            print(f"{num} x {i} = {resultado} -> Impar")


# Funcion para checar si un numero es positivo, negativo o cero
def checar_numero():
    num = int(input("Ingrese un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
        return False

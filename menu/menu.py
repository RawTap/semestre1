from module import (
    calificacion,
    checar_numero,
    menu_circulo,
    numero_negativo,
    numeros_primos,
    promedio_estudiantes,
    saludar,
    suma,
    tabla_multiplicar,
    visita,
)

opcion = "0"
while opcion != "11":
    print("---Menu de opciones:---")
    print("1. Ingresar un numero")
    print("2. Tabla de multiplicar")
    print("3. Numeros primos entre 1 y 100")
    print("4. Sumar 3 numeros")
    print("5. Saludar")
    print("6. Visita")
    print("7. Calificacion")
    print("8. Promedio de estudiantes")
    print("9. Menu de circulo")
    print("10. Checar si un numero es positivo, negativo o cero")
    print("11. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero_negativo()
    elif opcion == "2":
        num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        tabla_multiplicar(num)
    elif opcion == "3":
        numeros_primos()
    elif opcion == "4":
        dato1 = int(input("Ingrese el primer número: "))
        dato2 = int(input("Ingrese el segundo número: "))
        dato3 = int(input("Ingrese el tercer número: "))
        suma(dato1, dato2, dato3)
    elif opcion == "5":
        saludar()
    elif opcion == "6":
        nom = input("Ingrese su nombre: ")
        visita(nom)
    elif opcion == "7":
        promedio_estudiantes()
    elif opcion == "8":
        calificacion()
    elif opcion == "9":
        menu_circulo()
    elif opcion == "10":
        checar_numero()
    elif opcion == "11":
        print("Saliendo del programa.")
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

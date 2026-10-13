from module.basic import saludar, suma
from module.calificacion import calificacion
from module.clase import visita
from module.negativo import numero_negativo
from module.primo import numeros_primos
from module.promedio import promedio_estudiantes
from module.tabla import tabla_multiplicar

opcion = "0"
while opcion != "9":
    print("---Menu de opciones:---")
    print("1. Ingresar un numero")
    print("2. Tabla de multiplicar")
    print("3. Numeros primos entre 1 y 100")
    print("4. Sumar 3 numeros")
    print("5. Saludar")
    print("6. Visita")
    print("7. Calificacion")
    print("8. Promedio de estudiantes")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero_negativo()
    elif opcion == "2":
        tabla_multiplicar()
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
        print("Saliendo del programa.")
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

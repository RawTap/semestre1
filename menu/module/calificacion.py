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

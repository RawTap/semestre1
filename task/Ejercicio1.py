nota=int(input("Ingrese la calificacion del estudiante del 1-100: "))
if nota < 60:
    print("El estudiante obtuvo una F")
elif nota < 70:
    print("El estudiante obtuvo una D")
elif nota < 80:
    print("El estudiante obtuvo una C")
elif nota < 90:
    print("El estudiante obtuvo una B")
elif nota <= 100:
    print("El estudiante obtuvo una A")
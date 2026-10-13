numero = 1
suma_total = 0
cantidad_numero = 0
while numero != 0:
    numero = int(input("Ingrese un número: "))
    suma_total += numero
    cantidad_numero += 1
print(
    f"La suma de los números ingresados es: {suma_total} y se ingresaron {cantidad_numero} números"
)

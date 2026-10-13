numero = int(input("Ingrese el numero de 1 - 10: "))
resultado = 0
for i in range(1, 11):
    resultado = numero * i
    if resultado % 2 == 0:
        print(f"{numero} x {i} = {resultado} es par")
    else:
        print(f"{numero} x {i} = {resultado} es impar")

hola = "Hola,mundo!"

numero = int(input("Ingrese un numero "))
par = 0
inpar = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        par += 1
        print(f"El numero {i} es par")
    else:
        inpar += 1
        print(f"El numero {i} es impar")

print(f"La cantidad de numeros pares es: {par}")
print(f"La cantidad de numeros impares es: {inpar}")

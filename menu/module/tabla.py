def tabla_multiplicar():
    num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    for i in range(1, 11):
        resultado = num * i
        if resultado % 2 == 0:
            print(f"{num} x {i} = {resultado} -> Par")
        else:
            print(f"{num} x {i} = {resultado} -> Impar")

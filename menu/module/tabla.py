def tabla_multiplicar(num):
    for i in range(1, 11):
        resultado = num * i
        if resultado % 2 == 0:
            print(f"{num} x {i} = {resultado} -> Par")
        else:
            print(f"{num} x {i} = {resultado} -> Impar")

acumulador = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i % j == 0:
            acumulador += 1
            if i == j:
                break
    print(f"La cantidad de divisiones exactas es: {acumulador}")
    acumulador = 0

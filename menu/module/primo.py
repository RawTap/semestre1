def numeros_primos():
    print("Los numeros primos entre 1 y 100 son:")
    for num in range(2, 101):
        es_primo = True
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

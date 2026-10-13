def promedio_estudiantes():
    promedio_individual = 0.0
    promedio_global = 0.0
    for i in range(10):
        promedio_individual = 0.0
        for j in range(3):
            nota = float(
                input(
                    f"Ingrese la nota {j + 1} del estudiante {i + 1} en el rango de 1 al 10: "
                )
            )
            promedio_individual = promedio_individual + nota
        promedio_individual = promedio_individual / 3
        print(f"El promedio del estudiante {i + 1} es: {promedio_individual:.2f}")
        promedio_global = promedio_global + promedio_individual
    promedio_individual = 0
    print(f"El promedio global es: {promedio_global / 10:.2f}")

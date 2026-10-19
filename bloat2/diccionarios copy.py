asteroides_nasa = [
    {
        "id": "2099942",
        "name": "99942 Apophis",
        "estimated_diameter_km": 0.37,
        "is_potentially_hazardous": True,
        "close_approach_years": [2029, 2036, 2068],
    },
    {
        "id": "2001620",
        "name": "1620 Geographos",
        "estimated_diameter_km": 2.56,
        "is_potentially_hazardous": True,
        "close_approach_years": [2026, 2038],
    },
    {
        "id": "3102712",
        "name": "2002 MN",
        "estimated_diameter_km": 0.08,
        "is_potentially_hazardous": False,
        "close_approach_years": [2028],
    },
    {
        "id": "2004330",
        "name": "433 Eros",
        "estimated_diameter_km": 16.84,
        "is_potentially_hazardous": False,
        "close_approach_years": [2026, 2031, 2056],
    },
]


def mostrar_datos_asteroides(asteroides):
    for asteroide in asteroides:
        print(
            f"Nombre: {asteroide['name']}, "
            f"Diametro estimado: {asteroide['estimated_diameter_km']}, "
            f"Peligroso: {asteroide['is_potentially_hazardous']}, "
            f"Años de acercamiento: {asteroide['close_approach_years']}"
        )


def mostrar_asteroides_peligrosos(asteroides):
    """Muestra los asteroides potencialmente peligrosos."""
    print("\nAsteroides peligrosos:")
    print(r"""
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_|
""")
    for asteroide in asteroides:
        if asteroide["is_potentially_hazardous"]:
            print(f"El asteroide {asteroide['name']} es peligroso")


def mostrar_asteroides_por_anio(asteroides, anio):
    """Muestra los asteroides que se acercarán en un año determinado."""
    for asteroide in asteroides:
        if anio in asteroide["close_approach_years"]:
            print(
                f"\nEn {anio}, el asteroide {asteroide['name']} tendrá un "
                f"diámetro estimado de {asteroide['estimated_diameter_km']} km."
            )


def calcular_promedio_diametros(asteroides):
    """Calcula el promedio de los diámetros estimados."""
    suma_diametros = sum(asteroide["estimated_diameter_km"] for asteroide in asteroides)
    return suma_diametros / len(asteroides)


def main():
    mostrar_datos_asteroides(asteroides_nasa)
    mostrar_asteroides_peligrosos(asteroides_nasa)
    mostrar_asteroides_por_anio(asteroides_nasa, 2026)

    promedio = calcular_promedio_diametros(asteroides_nasa)
    print(
        f"La suma de los diámetros estimados de todos los asteroides es: {promedio} km."
    )


if __name__ == "__main__":
    main()

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
for asteroide in asteroides_nasa:
    print(
        f"Nombre: {asteroide['name']}, Diametro estimado: {asteroide['estimated_diameter_km']}, Peligroso: {asteroide['is_potentially_hazardous']}, Años de acercamiento: {asteroide['close_approach_years']}"
    )

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
for asteroide in asteroides_nasa:
    if asteroide["is_potentially_hazardous"]:
        print(f"El asteroide {asteroide['name']} es peligroso")

for asteroide2 in asteroides_nasa:
    if 2026 in asteroide2["close_approach_years"]:
        print(
            f"\nEn 2026, el asteroide {asteroide2['name']} tendrá un diámetro estimado de {asteroide2['estimated_diameter_km']} km."
        )

sumas = 0
for x in asteroides_nasa:
    sumas += x["estimated_diameter_km"]
print(
    f"La suma de los diámetros estimados de todos los asteroides es: {sumas / len(asteroides_nasa)} km."
)

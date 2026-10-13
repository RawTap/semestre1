import random

# datos
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerico = "0123456789"
vocales = "AEIOU"
nombres = ["JOSE", "MARIA"]
particulas_nombres = [
    "DA",
    "DAS",
    "DEL",
    "DER",
    "DI",
    "DIE",
    "DD",
    "EL",
    "LA",
    "LOS",
    "LAS",
    "LE",
    "LES",
    "MAC",
    "MC",
    "VAM",
    "VOM",
    "Y",
]

apellido_paterno = input("Ingrese su apellido paterno: ").upper()
apellido_materno = input("Ingrese su apellido materno: ").upper()
nombre_completo = input("Ingrese su nombre completo: ").upper().split()
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").split("/")

# parte paterna
letra_paterna = apellido_paterno[:1]
vocal_paterno = ""
for i in apellido_paterno[1:]:
    if i in vocales:
        vocal_paterno = i
        break
print(f"La primera parte del RFC es: {letra_paterna}{vocal_paterno}")

# parte materna
letra_materna = apellido_materno[:1]
if letra_materna == "":
    letra_materna = "X"
print(f"La segunda parte del RFC es: {letra_materna}")

# parte nombres
for i in nombre_completo:
    if i not in nombres and i not in particulas_nombres:
        letra_n = i[:1]
        break

print(f"La tercera parte del RFC es: {letra_n}")

# parte fecha
dia = fecha_nacimiento[0]
mes = fecha_nacimiento[1]
anio = fecha_nacimiento[2][2:]
print(f"La cuarta parte del RFC es: {anio}{mes}{dia}")

# parte homoclave
aleatorio_n = (
    random.choice(abecedario) + random.choice(abecedario) + random.choice(numerico)
)
print(f"La quinta parte del RFC es: {aleatorio_n}")

print(
    f"Su RFC completo es: {letra_paterna}{vocal_paterno}{letra_materna}{letra_n}{dia}{mes}{anio}{aleatorio_n}"
)

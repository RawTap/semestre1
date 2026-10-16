import random
from collections.abc import Sequence
from dataclasses import dataclass

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "0123456789"
VOCALES = "AEIOU"
NOMBRES_OMITIDOS = {"JOSE", "MARIA"}
PARTICULAS_NOMBRE = {
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
}
PALABRAS_SAT = {
    "BUEI",
    "BUEY",
    "CACA",
    "CACO",
    "CAGA",
    "CAGO",
    "CAKA",
    "CAKO",
    "COGE",
    "COJA",
    "COJE",
    "COJI",
    "COJO",
    "CULO",
    "FETO",
    "GUEY",
    "JOTO",
    "KACA",
    "KACO",
    "KAGA",
    "KAGO",
    "KAKA",
    "KOGE",
    "KOJO",
    "KULO",
    "MAME",
    "MAMO",
    "MEAR",
    "MEAS",
    "MEON",
    "MIAR",
    "MION",
    "MOCO",
    "MULA",
    "PEDA",
    "PEDO",
    "PENE",
    "PUTA",
    "PUTO",
    "QULO",
    "RATA",
    "RUIN",
}


def primera_vocal_interna(apellido: str) -> str:
    """Devuelve la primera vocal del apellido después de su inicial."""
    return next((letra for letra in apellido[1:] if letra in VOCALES), "")


def primera_inicial_valida(nombres: Sequence[str]) -> str:
    """Devuelve la inicial del primer nombre que no debe omitirse."""
    for nombre in nombres:
        if nombre not in NOMBRES_OMITIDOS and nombre not in PARTICULAS_NOMBRE:
            return nombre[:1]
    raise ValueError("No se encontró un nombre válido.")


@dataclass(frozen=True)
class PartesRFC:
    letras: str
    fecha: str
    homoclave: str
    fecha_salida: str
    palabra_sat: bool

    @property
    def completo(self) -> str:
        return f"{self.letras}{self.fecha_salida}{self.homoclave}"


def generar_homoclave() -> str:
    return random.choice(ALFABETO) + random.choice(ALFABETO) + random.choice(NUMEROS)


def generar_rfc(
    apellido_paterno: str,
    apellido_materno: str,
    nombres: Sequence[str],
    fecha_nacimiento: Sequence[str],
) -> PartesRFC:
    """Genera las cinco partes del RFC a partir de datos ya normalizados."""
    letra_paterna = apellido_paterno[:1]
    vocal_paterno = primera_vocal_interna(apellido_paterno)
    letra_materna = apellido_materno[:1] or "X"
    letra_nombre = primera_inicial_valida(nombres)

    primeras_letras = letra_paterna + vocal_paterno + letra_materna + letra_nombre
    palabra_sat = primeras_letras in PALABRAS_SAT
    if palabra_sat:
        letra_nombre = "X"

    dia, mes, anio = fecha_nacimiento
    fecha = anio[2:] + mes + dia
    homoclave = generar_homoclave()

    letras = letra_paterna + vocal_paterno + letra_materna + letra_nombre
    return PartesRFC(
        letras=letras,
        fecha=fecha,
        homoclave=homoclave,
        fecha_salida=dia + mes + anio[2:],
        palabra_sat=palabra_sat,
    )


def main() -> None:
    apellido_paterno = input("Ingrese su apellido paterno: ").upper()
    apellido_materno = input("Ingrese su apellido materno: ").upper()
    nombres = input("Ingrese su nombre completo: ").upper().split()
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").split("/")

    partes = generar_rfc(
        apellido_paterno,
        apellido_materno,
        nombres,
        fecha_nacimiento,
    )

    print(f"La primera parte del RFC es: {partes.letras[:2]}")
    print(f"La segunda parte del RFC es: {partes.letras[2]}")
    print(f"La tercera parte del RFC es: {partes.letras[3]}")
    if partes.palabra_sat:
        print("La tercera parte del RFC es: X")
    print(f"La cuarta parte del RFC es: {partes.fecha}")
    print(f"La quinta parte del RFC es: {partes.homoclave}")
    print(f"Su RFC completo es: {partes.completo}")


if __name__ == "__main__":
    main()

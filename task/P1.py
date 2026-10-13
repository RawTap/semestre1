edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

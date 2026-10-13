frase="Hello, World!"
vocal="AEIOUaeiou"
letra=0 
for i in frase:
    if i in vocal:
       letra += 1 
print("La cantidad de vocales es:", letra)


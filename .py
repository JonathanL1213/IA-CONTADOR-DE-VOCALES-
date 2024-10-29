# Solicitar al usuario que ingrese una frase
frase = input("Escribe una frase: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Recorrer cada carácter en la frase
for letra in frase:
    # Comprobar si el carácter es una vocal
    if letra in vocales:
        contador_vocales += 1

# Imprimir el resultado
print("La cantidad de vocales en la frase es: ", contador_vocales)

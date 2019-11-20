# Enrique Rojas - p07e12
# Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un solo blanco.

def cuenta_palabras(a):
    palabras = 0
    palabras = a.count(" ") + 1
    return palabras
frase = input("Escribe una frase: ")
print (f"Has escrito {cuenta_palabras(frase)} palabras")
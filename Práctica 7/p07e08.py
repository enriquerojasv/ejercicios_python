# Enrique Rojas - p07e08
# Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.

frase = input("Ecribe una frase: ")
def espacioAsterisco(a):
    return a.replace(" ", "")
print (espacioAsterisco(frase))
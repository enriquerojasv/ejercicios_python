# Enrique Rojas - p07e05
# Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá.

frase = input("Dime algo: ")
vocal = input("Dime una vocal: ")
def cambiaVocal(a):
    return a.replace("a","e").replace("i","e").replace("o","e").replace("u","e").replace("e",f"{vocal}")
print (cambiaVocal(frase))
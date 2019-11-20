# Enrique Rojas - p07e06
# Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.

nombre = input("Escribe un nombre: ")
caracter = input("Dime un caracter: ")
def buscaCaracter(a):
    if a.find(caracter)==-1:
        return "El caracter no aparece en el nombre"
    else:
        return "El caracter sí aparece en el nombre"
print (buscaCaracter(nombre))
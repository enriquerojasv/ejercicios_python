# Enrique Rojas - p07e02
# Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.

nom = input("Escribe tu nombre con los dos apellidos: ")
def sinEspacio(a):
    return a.replace(" ", "")
print (sinEspacio(nom))
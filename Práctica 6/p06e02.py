# Enrique Rojas - p06e02
# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.

numeros = int(input("Escribe un número "))
lista = []
while numeros!="Salir":
    lista.append(numeros)
    numeros=input("Escribe más números ")
print("Los números que has introducido son ", lista)
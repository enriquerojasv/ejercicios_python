# Enrique Rojas - p06e01
# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.

palabras = input("Escribe una palabra ")
lista = []
while palabras!="":
    lista.append(palabras)
    palabras=input("Escribe más palabras ")
print("Las palabras que has escrito son ", lista)
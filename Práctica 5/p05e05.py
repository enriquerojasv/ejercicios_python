# Enrique Rojas - p05e05
# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje.

anchura = int(input("Introduzca la anchura del rectángulo "))
altura = int(input("Introduzca la altura del rectángulo "))
for i in range(altura):
    if i > 0:
        print ("")
    for j in range(anchura):
        print ("*", end='')

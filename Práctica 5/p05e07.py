# Enrique Rojas - p05e07
# Escribe un programa que pida la altura de un triángulo y lo dibuje.

altura = int(input("Introduzca la altura del triángulo "))
for i in range(altura,0,-1):
    print ("*"*i, end='')
    print ("")

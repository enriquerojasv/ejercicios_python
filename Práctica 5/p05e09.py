# Enrique Rojas - p05e09
# Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje.

anchura = int(input("Introduce la anchura del rectángulo "))
altura = int(input("Introduce la altura del rectángulo "))
for i in range(1,altura+1):
    if i == 1 or i == altura:
        print (anchura*("*"))
    else:
        print ("*", (anchura-4)*" ", "*")





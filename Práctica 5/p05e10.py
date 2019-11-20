# Enrique Rojas - p05e10
# Escribe un programa que pida la altura de un triángulo y lo dibuje.

altura = int(input("Inserta la altura de un triángulo "))
for i in range(1,altura+1):
    print ((altura-i)*" ",(i*2-1)*"*")

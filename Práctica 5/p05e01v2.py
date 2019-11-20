# Enrique Rojas - p05e01 v2
# Escribe un programa que escriba a los siguientes número (la separación entre número es para facilitar cuántos números se deben escribir en cada bucle) y en el que la función range que utilices tenga un ÚNICO argumento y que el valor de este se corresponda con el número de elementos que aparecen en la lista

for i in range (10):
    print (i+1,end='')
print("")

for i in range (10):
    print (((i+1)*2),end='')
print("")

for i in range (10):
    i=i+i+20
    print (i,end='')
print("")

for i in range (6):
    i=(i*4)+10
    print (i,end='')
print("")

for i in range (9):
    n=(i*5)
    i=(i+40-i)-n
    print (i,end='')

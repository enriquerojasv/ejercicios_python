# Enrique Rojas - p04e02
# Pida al usuario 5 números y diga si estos estaban en orden decreciente, creciente o desordenados.

a = int(input("Introduzca un número "))
b = int(input("Introduzca otro número "))
c = int(input("Introduzca otro número "))
d = int(input("Introduzca otro número "))
e = int(input("Introduzca un último número "))
if a>b and b>c and c>d and d>e:
    print ("Los números están en orden decreciente")
elif a<b and b<c and c<d and d<e:
    print ("Los números están en orden creciente")
else:
    print ("Los números están desordenados")

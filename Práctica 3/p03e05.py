# Enrique Rojas - P03E05
# Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.
A= int(input("Introduce un número de tres cifras "))
if A<0 or A>999:
    print ("ERROR: El número", A, " tiene más de tres cifras")
else:
    print ("Ok")

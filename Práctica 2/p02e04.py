# Enrique Rojas - P02E04
# Diagrama para calcular el mayor de dos números
A = int(input("Introduce un número: "))
B = int(input("Introduce otro número: "))
if A > B:
    print (f"{A} es mayor")
if B > A:
    print (f"{B} es mayor")
if A == B:
    print ("Los dos números son iguales")
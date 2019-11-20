# Enrique Rojas - p05e11
# Escribe un programa que pida un número e imprima todos sus divisores.

num = int(input("Dame un número "))
for i in range (1,num+1):
    if ((num%i)==0):
        print (i)

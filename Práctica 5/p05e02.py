# Enrique Rojas - p05e02
# Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares.

num_a = int(input("Escribe un número "))
num_b = int(input("Escribe otro número "))
if num_a <= num_b:
    for i in range(num_a,num_b+1):
        if i%2==0:
            print ("El número ", i, " es par")
        else:
            print ("El número ", i, " es impar")
if num_b < num_a:
    for i in range(num_b,num_a+1):
        if i%2==0:
            print ("El número ", i, " es par")
        else:
            print ("El número ", i, " es impar")
                

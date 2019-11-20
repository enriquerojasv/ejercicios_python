# Enrique Rojas - p06e04
# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide.

num_a = int(input("Escribe un número: "))
num_b = int(input(f"Escribe un número mayor que {num_a}: "))
while num_a>=num_b:
    num_b = int(input(f"{num_b} no es mayor que {num_a}. Vuelve a introducir un número: "))
print (f"Los números que has escrito son {num_a} y {num_b}")

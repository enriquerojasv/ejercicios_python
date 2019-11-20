# Enrique Rojas - p06e06
# Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.

num_a = int(input("Escribe un número: "))
num_b = int(input(f"Escribe un número mayor que {num_a}: "))
num_c = num_a + 1
lista = []
while num_a>=num_b:
    num_b = int(input(f"{num_b} no es mayor que {num_a}. Vuelve a introducir un número: "))
while num_c>num_a and num_c<num_b:
    num_c = int(input(f"Escribe un número entre {num_a} y {num_b}: "))
    if num_c>num_a and num_c<num_b:
        lista.append(num_c)
lista_string=str(lista[0])
for i in range (1,len(lista)):
    lista_string += ", "+str(lista[i])
print (f"Los números situados entre {num_a} y {num_b} que has escrito son: ", lista_string)
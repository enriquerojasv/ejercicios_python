# Enrique Rojas - p06e05
# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números.

num_a = int(input("Escribe un número: "))
lista = [num_a]
num_b = num_a+1
num_c = num_a
while num_b > num_a:
    num_a = num_b
    num_b = int(input(f"Escribe un número mayor que {num_c}: "))
    if num_b > num_a:
        lista.append(num_b)
    num_c = num_b
lista_string = str(lista[0])
for i in range(1,len(lista)):
   lista_string += ", "+str(lista[i])
print ("Los números que has escrito son:", lista_string)
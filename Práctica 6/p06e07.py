# Enrique Rojas - p06e07
# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.

limite = int(input("Escribe límite: "))
suma_valor = 0
lista = []
while limite >= suma_valor:
    valor = int(input("Escribe un valor: "))
    lista.append(valor)
    suma_valor += valor
lista_string = str(lista[0])
for i in range (1, len(lista)):
    lista_string += ", "+str(lista[i])
print (f"El límite a superar es {limite}. La lista creada es {lista_string} ya que la suma de estos números es: {suma_valor}")

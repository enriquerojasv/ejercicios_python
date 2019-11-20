# Enrique Rojas - p06e08
# Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

# =============== PENDIENTE SIMPLIFICAR ==================

limite = int(input("Escribe límite: "))
suma_valor = 0
lista = []
while limite > suma_valor:
    valor = int(input("Escribe un valor: "))
    suma_valor += valor
    if limite >= suma_valor:
        lista.append(valor)
    if suma_valor > limite:
        while suma_valor > limite:
            suma_valor -= valor
            valor = int(input(f"{valor} es demasiado grande. Escribe otro valor: "))
            suma_valor += valor
        lista.append(valor)
lista_string = str(lista[0])
for i in range (1,len(lista)):
    lista_string += ", " + str(lista[i])
print (f"El límite a alcanzar es {limite}. La lista creada es: {lista_string}")


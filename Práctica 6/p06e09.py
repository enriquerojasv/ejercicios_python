# Enrique Rojas - p06e09
# Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.

nom = input("Dame un nombre: ")
lista = []
while nom != "s" and nom != ("S"):
    tel = input("Dame el teléfono: ")
    sub_lista = [nom, tel]
    lista.append(sub_lista)
    nom = input("Dame un nombre: ")
print ("Los nombres y teléfonos de la agenda son:")
for i in range (len(lista)):
    print (lista[i][0] + ": " + lista[i][1])   
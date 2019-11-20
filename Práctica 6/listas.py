lista = []
sub_lista = ["aaa", 1111]
lista.append(sub_lista)
sub_lista = ["bbb", 2222]
lista.append(sub_lista)
sub_lista = ["cccc", 3333]
lista.append(sub_lista)

# for i in lista:
#     print (": ".join[i])
# lista_string=""
for i in range (len(lista)):
    for j in range (len(lista[i])):
        print (lista[i][j])

for i in range (len(lista)):
    for j in lista[i]:
        print (j,end="")

# lista_string= ""
# for i in range (len(lista)):
#    if i%2 == 0:
#        lista_string += str(lista[i]) + ": "
#    else:
#        lista_string += str(lista[i])
#     for j in range (i+1, i+1):
#        lista_string += str(lista[i])
#      print (lista_string)



#lista_string = ""
#for i in range (0,1):
#    lista_string += ": " + str(lista[i])
#print ("Los nombres y teléfonos de la agenda son: ", lista_string)
    
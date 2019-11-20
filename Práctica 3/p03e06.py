# Enrique Rojas - P03E06
# Pida al usuario el precio de un producto y el nombre del producto y muestre el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.
P= int(input("Introduce el precio de un producto "))
N= input("Introduce el nombre del produto ")
R= P+((P*21)/100)
print ("Tu ", N, " vale ", P, " euros y con el 21% de IVA se queda en ", R, " euros en total.")

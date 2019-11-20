# Enrique Rojas - p04e05
# Pida al usuario un importe en euros y diga si el cajero automático le puede dar dicho importe utilizando el mismo billete y el más grande.

importe = int(input("Introduce un importe en euros "))
vuelta = int
if importe%500==0:
    vuelta = importe/500
    print ("el cajero te devuelve ", vuelta, " billetes de 500 euros")
elif importe%200==0:
    vuelta = importe/200
    print ("el cajero te devuelve ", vuelta, " billetes de 200 euros")
elif importe%100==0:
    vuelta = importe/100
    print ("el cajero te devuelve ", vuelta, " billetes de 100 euros")
elif importe%50==0:
    vuelta = importe/50
    print ("el cajero te devuelve ", vuelta, " billetes de 50 euros")
elif importe%20==0:
    vuelta = importe/20
    print ("el cajero te devuelve ", vuelta, " billetes de 20 euros")
elif importe%10==0:
    vuelta = importe/10
    print ("el cajero te devuelve ", vuelta, " billetes de 10 euros")
elif importe%5==0:
    vuelta = importe/5
    print ("el cajero te devuelve ", vuelta, " billetes de 5 euros")
else:
    print ("no se le puede dar dicho importe solo en billetes")
    
              

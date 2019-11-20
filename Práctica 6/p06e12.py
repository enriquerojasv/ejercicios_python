# Enrique Rojas - p06e12
# Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.

#==== FALTA UN APARTADO DE LO OPCIONAL ====

import random
import time
random.seed (time.time ())
mini = int (input ("Valor mínimo: "))
maxi = int (input ("Valor máximo: "))
while mini >= maxi:
    print ("No hagas trampas y ponlo bien, saco de carne")
    mini = int (input ("Valor mínimo: "))
    maxi = int (input ("Valor máximo: "))
print (f"Piensa un número entre {mini} y {maxi} a ver si lo puedo adivinar.")
adiv = (random.randint (mini, maxi))
pause = input("Pulsa intro cuando hayas conseguido pensar un número, simple humano ")
respuesta = input(f"Es {adiv}? ")
while respuesta != "igual":
    if respuesta == "mayor":
        mini = adiv+1
    if respuesta == "menor":
        maxi = adiv-1
    adiv = (random.randint (mini, maxi))
    respuesta = input(f"Es {adiv}? ")
print ("¡Gracias por jugar con tu amigo robotito!")
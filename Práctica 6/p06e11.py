# Enrique Rojas - p06e11
# Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños.

import random
import time
random.seed (time.time ())
mini = int (input ( "Valor mínimo: "))
maxi = int (input ( "Valor máximo: "))
secreto = random.randint (mini, maxi)
print (f"A ver si adivinas un número entero entre {mini} y {maxi}.")
numero = int
numero = int(input("Escribe un número: "))
intentos = 1
while numero != secreto:
    if numero > secreto:
        intentos += 1
        numero = int(input("¡Demasiado grande! Volver a probar: "))
    if numero < secreto:
        intentos += 1
        numero = int(input("¡Demasiado pequeño! Volver a probar: "))
if intentos == 1:
    print ("¡A la primera!")
else:
    print (f"¡Correcto! Lo has intentado {intentos} veces.")
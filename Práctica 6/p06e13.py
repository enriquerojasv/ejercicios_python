# Enrique Rojas - p05e12
# Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

num = int(input("Dame un número "))
if num<2:
        print ("Debe ser un número natural mayor que 1")
base = 2
while num%base!=0 and base<num:
    base += 1
if base == num:
    print (f"El número {num} es primo")
else:
    print (f"El número {num} no es primo")

# Es más eficiente utilizar un while que un for, en tanto que el while para en el momento que no se cumple la condición que se le ha establecido
# mientras que el for realizará todo el recorrido si no se le explicita interrumpirlo antes con un break.
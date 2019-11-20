# Enrique Rojas - p04e04
# Pida al usuario tres números y un cuarto número, y compruebe si éste último es divisor de los tres números primeros.

a = int(input("Introduzca un número "))
b = int(input("Introduzca otro número "))
c = int(input("Introduzca otro número "))
d = int(input("Introduzca un último número para comprobar si es divisor de los anteriores "))
if (a%d)==0 and (b%d)==0 and (c%d)==0: 
    print ("Es divisor de todos")
elif (a%d)==0 and not(b%d)==0 and not(c%d)==0:
    print ("Es divisor de ", a)
elif (a%d)==0 and (b%d)==0 and not(c%d)==0:
    print ("Es divisor de ", a, " y ", b)
elif (a%d)==0 and (c%d)==0 and not(b%d)==0:
    print ("Es divisor de ", a, " y ", c)
elif (b%d)==0 and not(a%d)==0 and not(c%d)==0:
    print ("Es divisor de ", b)
elif (b%d)==0 and (c%d)==0 and not(a%d)==0:
    print ("Es divisor de ", b, " y ", c)
elif (c%d)==0 and not(a%d)==0 and not(b%d)==0:
    print ("Es divisor de ", c)
else:
    print ("No es divisor")

# Enrique Rojas - p07e13
# Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, por tanto, habrán dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra (con while). Ambas funciones devolverá true (si es es primo) o false (si no es primo). El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra.

def primo_for(a):
    primo = True
    if a<2:
        print ("Debe ser un número natural mayor que 1")
    else:
        for i in range(2,a+1):
            if i<a and a%i==0:
                primo = False        
        if primo == True:
            return True
        if primo == False:
            return False

def primo_while(a):
    if a<2:
        print ("Debe ser un número natural mayor que 1")
    base = 2
    while a%base!=0 and base<a:
        base += 1
    if base == a:
        return True
    else:
        return False

num = int(input("Escribe un número: "))
elige = input("Elige si quieres calcular con 'for' o con 'while': ")
if elige == "for":
    print (primo_for(num))
if elige == "while":
    print (primo_while(num))
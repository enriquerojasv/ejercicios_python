# Enrique Rojas - p05e12
# Escribe un programa que pida un número y escriba si es primo o no.

num = int(input("Dame un número "))
primo = True
if num<2:
        print ("Debe ser un número natural mayor que 1")
else:
    for i in range(2,num+1):
        if i<num and num%i==0:
            primo = False        
    if primo == True:
        print (f"El número {num} es primo")
    if primo == False:
        print (f"El número {num} no es primo")
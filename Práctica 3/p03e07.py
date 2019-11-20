# Enrique Rojas - p03e07
# Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.  Por ejemplo: 
# 32/01/2017->Fecha incorrecta
# 29/02/2017->Fecha incorrecta
# 30/09/2017->Fecha correcta.
dia = int(input("Introduzca un día "))
mes = int(input("Introduzca un mes "))
año = int(input("Introduzca un año "))
if año<0 or año>9999 or dia<1 or dia>31 or mes<1 or mes>12:
    print ("Fecha incorrecta")
elif mes==2 and dia>28:
    print ("Fecha incorrecta")
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        print ("Fecha incorrecta")
else:
    print ("Fecha correcta")


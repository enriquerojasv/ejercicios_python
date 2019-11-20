# Enrique Rojas - p07e09
# Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

def rimador(a,b):
    palabra1lar = a[-3:]
    palabra2lar = b[-3:]
    palabra1cor = a[-2:]
    palabra2cor = b[-2:]
    if palabra1lar == palabra2lar:
        print (f"Las palabras {palabra1} y {palabra2} riman")
        pass
    if (palabra1lar != palabra2lar) and (palabra1cor == palabra2cor):
        print (f"Las palabras {palabra1} y {palabra2} riman un poco")
    else:
        print (f"Las palabras {palabra1} y {palabra2} no riman")    
palabra1 = input("Escribe una palabra: ")
palabra2 = input("Escribe otra palabra: ")
(rimador(palabra1,palabra2))

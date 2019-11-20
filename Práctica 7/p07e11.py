# Enrique Rojas - p07e11
# Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es palíndroma o no , y el programa principal escribirá el resultado por pantalla.

def palindromo(a):
    alreves = ""
    for i in range(len(a)-1,-1,-1):
        alreves += (a[i])
    if alreves == a:
        return f"{a} es palíndromo"
    else:
        return f"{a} no es palíndromo"
a = input("Escribe una frase: ")
print (palindromo(a))
# Enrique Rojas - p07e10
# Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función.

def capicuaPalindromo(a):
    alreves = ""
    for i in range(len(a)-1,-1,-1):
        alreves += (a[i])
    if alreves == a:
        return f"{a} es palíndromo o capicúa"
    else:
        return f"{a} no es palíndromo ni capicúa"
a = input("Escribe una palabra o un número: ")
print (capicuaPalindromo(a))
# Enrique Rojas - p07e03
# Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

frase = input("Escribe una frase: ")
def lineas(a):
    for i in range(len(a)):
        print (a[i])
lineas(frase)
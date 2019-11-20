# Enrique Rojas - p07e01
# Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

texto = input("Escribe un texto: ")
def minusMayus(a):
    print (a.lower())
    print (a.upper())
minusMayus(texto)
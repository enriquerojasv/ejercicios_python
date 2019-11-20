# Enrique Rojas - p07e07
# Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

frase = input("Escribe una frase: ")
va = 0
ve = 0
vi = 0
vo = 0
vu = 0
def cuentaVocales(a):
    a = a.lower()
    va = a.count("a")
    ve = a.count("e")
    vi = a.count("i")
    vo = a.count("o")
    vu = a.count("u")
    print (f"En la frase aparecen {va} 'a', {ve} 'e', {vi} 'i', {vo} 'o' y {vu} 'u'.")
(cuentaVocales(frase))
# Enrique Rojas - p06e10
# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

#==== PENDIENTE IMPRESIÓN CORRECTA ====

nom = input("Dame un nombre: ")
lista = []
while nom !="":
    sub_lista = [nom]
    nota = float(input("Escribe una nota: "))
    while nota <= 10 and nota >= 0:
        sub_lista.append(nota)
        nota = float(input("Escribe otra nota: "))
    lista.append(sub_lista)
    nom = input("Dame un nombre: ")
print ("Las notas de los alumnos son:")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == 0:
            print (lista[i][j],": ")
        elif j > 0 and j < (len(lista[i])-1):
            print (lista[i][j]," - ")
        else:
            print (lista[i][j])
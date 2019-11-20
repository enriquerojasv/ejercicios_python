# Enrique Rojas - p06e03
# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

notas = float(input("Escribe una nota: "))
lista = []
while notas<=10 and notas>=0:
    lista.append(notas)
    notas=float(input("Escribe otra nota: "))
print("Las notas que has escrito son:", lista)

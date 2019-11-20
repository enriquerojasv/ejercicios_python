# Enrique Rojas - p07e14
# Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, que recibe como parámetro la fecha en números y devuelve la fecha con el nombre del mes.

d = {
1: "enero",
2: "febrero",
3: "marzo",
4: "abril",
5: "mayo",
6: "junio",
7: "julio",
8: "agosto",
9: "septiembre",
10: "octubre",
11: "noviembre",
12: "diciembre"}

def fecha_palabra(a):
    mes=(fecha[3:5])
    int_mes = int(mes)
    print (fecha[0:2],"de",d[int_mes],"de",fecha[6:])

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
(fecha_palabra(fecha))
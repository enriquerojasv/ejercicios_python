# Enrique Rojas - p04e03
# Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.

pedido = input("Quiere calcular el área de un triángulo o de un cuadrado? ")
if pedido == "Triángulo" or pedido == "triángulo" or pedido == "Triangulo" or pedido == "triangulo":
    b_triangulo = int(input("Introduzca la base del triángulo "))
    h_triangulo = int(input("Introduzca la altura del triángulo "))
    a_triangulo = (b_triangulo*h_triangulo)/2
    print ("El área del triángulo es ", a_triangulo)
if pedido == "Cuadrado" or pedido == "cuadrado":
    l_cuadrado = int(input("Introduzca el lado de un cuadrado "))
    a_cuadrado = l_cuadrado*l_cuadrado
    print ("El área del cuadrado es ", a_cuadrado)
else:
    print ("Solo se admiten triángulo y cuadrado")
        

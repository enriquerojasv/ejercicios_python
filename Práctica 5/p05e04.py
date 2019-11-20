# Enrique Rojas - p05e04
# Escribe un programa que pida un número y calcule su factorial.

num = int(input("Dame un número "))
resultado = 1
for i in range(1,num+1):
    resultado = i * resultado
print (f"El factorial de {num} es {resultado}")

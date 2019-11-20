# Enrique Rojas - p05e03
# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

num_a = int(input("Dame un número "))
num_b = int(input(f"Dame un número mayor que {num_a} "))
result = 0
for i in range(num_a,num_b+1):
    result = (result+i)
print (f"La suma desde {num_a} hasta {num_b} es: {result}")


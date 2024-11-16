#Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10

numero = int(input("Ingresa un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
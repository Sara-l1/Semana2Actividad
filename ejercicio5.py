#Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.

n1 = int(input("Dame un primer numero "))
n2 = int(input("Dame un segundo numero "))

suma = (n1 + n2)
resta = (n1 - n2)
multiplicacion = (n1 * n2)
division = (n1 / n2)

print(f"Con los numeros seleccionados, la suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion} y la division es {division}")
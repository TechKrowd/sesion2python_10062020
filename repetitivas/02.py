"""
Pedir dos números por teclado. Si el primero es mayor que el segundo, 
intercambiarlos. 
Mostrar todos los números pares comprendidos entre ambos.
"""

a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

if a > b:
	a, b = b, a

for i in range(a,b+1):
	if i % 2 == 0:
		print(i)

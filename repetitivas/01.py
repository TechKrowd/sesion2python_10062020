"""
Pedir N números enteros por teclado y obtener su suma. El valor de 
N también se pedirá por teclado y se validará que sea mayor a 0.
"""

n = int(input("¿Cuántos números quieres leer?"))

suma = 0
if n > 0:
	for i in range(n):
		x = int(input("Introduce un número:"))
		suma += x
	print("La suma es {}".format(suma))
else:
	print("El número introducido debe ser mayor a 0.")
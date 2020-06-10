""" 
Pedir dos números por teclado y comprobar si la división del 
primero entre el segundo es exacta y evitar divisiones entre 0.
"""

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

if n2 == 0:
	print("División entre 0")
elif n1 % n2 == 0:
	print("División exacta")
else:
	print("No es división exacta. Resto: {}".format(n1%n2))
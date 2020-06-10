"""
Pedir 3 números por teclado y comprobar que el primero sea menor 
que el segundo y que el tercero esté comprendido entre los dos 
anteriores.
"""

a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))
c = int(input("Introduce el tercer número: "))

if a < b:
	if c > a and c < b:
		print(f"{c} está entre {a} y {b}")
	else:
		print(f"{c} está entre {a} y {b}")
else:
	print(f"{a} no es menor que {b}")
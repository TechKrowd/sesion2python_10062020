"""
Pedir 3 números por teclado y comprobar si son los 3 iguales, 
hay 2 iguales o los 3 son diferentes.
"""

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

if a == b and a == c:
	print("3 iguales")
elif a==b or a==c or b==c:
	print("2 iguales")
else:
	print("3 diferentes")
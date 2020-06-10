"""
Pedir 10 números por teclado y mostrar un mensaje cada vez que se 
introduzca un número igual al anterior introducido.
"""
anterior = 0
for i in range(10):
	n = int(input("Introduce un número: "))
	if i > 0 and n == anterior:
		print("Has introducido el mismo que antes.")

	anterior = n
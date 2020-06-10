"""
Pedir un año por teclado y decir si es bisiesto. Un año es bisiesto 
si es divisible entre 4, pero no entre 100. 
Si también lo es de 100 debe ser divisible entre 400 para que 
sea bisiesto.
"""

year = 2019

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400:
			print("Bisiesto")
		else:
			print("No bisiesto")
	else:
		print("Bisiesto")
else:
	print ("No bisiesto")
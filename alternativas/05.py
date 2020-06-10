"""
Pedir un mes por teclado en formato numérico (1, 2, 3, etc.) 
y mostrar por pantalla cuántos días tiene (30, 31 o 28).
"""

mes = int(input("Introduce un mes:"))

if mes>0 and mes<13:
	if mes in (1,3,5,7,8,10,12):
		print("31 días")
	elif mes == 2:
		print("28 días")
	else:
		print("30 días")
else:
	print("No has introducido un mes válido.")
"""
A lo largo del día se mide la temperatura 10 veces. 
Pedir los datos por teclado y mostrar cuántas de esas muestras 
son positivas, cuántas negativas y cuántas 0. 
También se quiere conocer la temperatura máxima y la mínima.
"""

p = 0
n = 0
c = 0
maxima = 0
minima = 0

for i in range(1,11):
	t = float(input("Introduce la temperatura {}".format(i)))

	if i == 1 or t > maxima:
		maxima = t
	if i == 1 or t < minima:
		minima = t
	if t > 0:
		p += 1
	elif t < 0:
		n += 1
	else:
		c += 1

print("Máxima: %.2f"%(maxima))
print("Mínima: %.2f"%(minima))
print("Positivas: %d"%(p))
print("Negativas: %d"%(n))
print("Cero: %d"%(c))
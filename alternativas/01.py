"""
Pedir un número por teclado y comprobar si está 
comprendido entre 1 y 10.
"""

n = int(input("Introduce un número: "))

print("Si") if n>=1 and n<=10 else print("No")
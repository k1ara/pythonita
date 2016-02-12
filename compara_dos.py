#comparar dos números - Indicar el mayor de ellos.

N1 = int(raw_input("Indicar el primer número: "))
N2 = int(raw_input("Indicar el segundo número: "))

if N1 > N2:
	print str(N1)" "+"es mayor que"+" "str(N2)
else
	print str(N2)" "+"es menor que"+" "str(N1)
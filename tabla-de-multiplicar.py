#tabla de multiplicar N veces y N numero.

numero = int(raw_input("Ingresar numero de tabla de multiplicar: "))

for x in range(0,11):
	respuesta = (x*numero)
	print str(x) + "*" + str(numero)+ "=" + str(respuesta)
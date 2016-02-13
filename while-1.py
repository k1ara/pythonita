#Primer programa while donde se dara un numero y luego se "adivinara" indicando si esta cerca o lejos.

NUM = int(raw_input("Ingresar el numero principal: "))
N1 = int(raw_input("Intenta escribir el numero principal: "))

while N1 != NUM:
	if N1 > NUM:
		N1 = int(raw_input("Intenta elegir un numero menor: "))
	else:
		N1 = int(raw_input("Intenta elegir un numero mayor."))
print "Haz hacertado!"
#comparar tres numeros - Los coloca en orden de mayor a menor.

N1 = int(raw_input("Indicar el primer numero: "))
N2 = int(raw_input("Indicar el segundo numero: "))
N3 = int(raw_input("Indicar el tercer numero: "))

if N1 > N2:
	if N1 > N3:
		if N2 > N3:
			print str(N1)+ "-"+str(N2)+"-"+str(N3)
		else:
			print str(N1)+ "-"+str(N3)+"-"+str(N2)
	else:
		print str(N3)+ "-"+str(N1)+"-"+str(N2)
else:
	if N2 > N3:
		if N1 > N3:
			print str(N2)+ "-"+str(N1)+"-"+str(N3)
		else:
			print str(N2)+ "-"+str(N3)+"-"+str(N1)
	else:
		print str(N3)+ "-"+str(N2)+"-"+str(N1)
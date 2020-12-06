##Se realiza dos for donde una realiza los espacios y otro realiza las operaciones
for i in range(1,20+1,1):
	for contador in range(1,10,1):
		operacion = i * contador
		print("%d x %d = %d\n"% (i, contador, operacion))
	print("\n")	



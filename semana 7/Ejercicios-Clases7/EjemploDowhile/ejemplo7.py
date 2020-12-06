##Se raliza una condicion de repeticion donde se realizan todas las tablas hasta el 10 
contador = 1
while (contador <= 5):
	for i in range(1,10):
		operacion = i * contador
		print("%d x %d = %d\n"% (contador, i, operacion))
	print("\n")	
	contador = contador + 1	




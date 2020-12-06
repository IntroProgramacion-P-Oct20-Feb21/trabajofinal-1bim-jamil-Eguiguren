##Se tiene una condicion donde se realiza una tabla segun el numero que ingresen
contador = 1
tabla = int(input("Ingrese la tabla a generar: "))
while (contador <= 10):
	operacion = tabla * contador
	print("%d x %d = %d\n"% (tabla, contador, operacion))
	contador = contador + 1




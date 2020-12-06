##Se utilisa la condicion for para poder realizar todas las tablas del numero ingresado
tabla = int(input("Ingrese el la tabla a generar: "))
for contador in  range(5,30+1,1):
	operacion = tabla * contador
	print("%d x %d = %d\n"% (tabla, contador, operacion))



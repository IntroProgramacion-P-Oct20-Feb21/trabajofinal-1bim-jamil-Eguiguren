##Se realizo una cadena repetitiva para que se pueda presentar las tablas de multiplicar
limite_tabla = 12
contador = 1
tabla = int(input("Ingrese el número de tabla a generar: "))
print("Tabla de multiplicar del: %s\n"% (tabla))
while (contador <= 12):
	operacion = tabla * contador
	print("%d*%d=%d\n"% (\
		tabla,\
		contador,\
		operacion))
	contador = contador + 1


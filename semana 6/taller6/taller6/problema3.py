##Se realiza una condicion de repeticion la que permite realizar una tabla con los valores ingresados
contador = "si"
cadenafinal = ""
while (contador==("si")):
	nombre = input("Ingresar el nombre del empleado: ")
	numerodias = int(input("Ingresar el número de días trabajados: "))
	costodia = float(input("Ingresar el costo del dia trabajado: "))
	cancelar = costodia*numerodias
	cadenafinal = ("%s%s\t%d\t$.2f\t\t$%.2f\n"%(nombre,numerodias,costodia,cancelar))
	contador = input("Ingrese si, si decea colocar mas empleados\no\nIngrese no, si decea ver la tabla: ")
print ("%s\n"%(cadenafinal))	













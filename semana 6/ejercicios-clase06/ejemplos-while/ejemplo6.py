#Se genera una condicion para que el usuario decida cuantas variables decea ingresar
suma_total = 0
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
	calificacion = float(input("Ingrese calificación: "))
	suma_total = suma_total + calificacion
	temporal = int(input("Ingrese el valor de -1 para salir del ciclo: \n"))
	if (temporal== -1):
		bandera = False
print("El premedio total de calificaciones es %.2f\n"% (suma_total))





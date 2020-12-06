##Se realiza una condicion de repeticion la cual se realiza hasta que el usuario lo pida 
suma_total = 0
bandera = True
contador = 0
print("Ingrese las notas de los estudiantes de su materia: ")
while (bandera):
	calificacion = float(input("Ingrese calificación número: "))
	suma_total = suma_total + calificacion
	contador = contador + 1
	temporal = int(input("Ingrese el valor de -1 para salir del ciclo\n"))
	if(temporal== -1):
		bandera = False
promedio_final = suma_total / contador
print("El promedio final es %.2f\n"% (promedio_final))		










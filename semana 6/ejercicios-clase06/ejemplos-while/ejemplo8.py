##Se realiza una condicion bandera para que el usuario pueda decidir cuando quiera salir del ciclo
contador = 0
suma_total = 0
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
	calificacion=float(input("Ingrese calificación: "))
	suma_total = suma_total + calificacion
	contador = contador + 1
	temporal=(input("Ingrese si(salir)"))
	if (temporal==("si")):
		bandera = False
promedio_final = suma_total / contador
print("El promedio final es %.2f\n"% (promedio_final))




	




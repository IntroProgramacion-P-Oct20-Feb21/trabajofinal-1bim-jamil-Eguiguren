##Se va apresentar una tabla con las calificaciones que se ingresaron
cadenaFinal = ""
bandera = True
while(bandera):
	nota = float(input("Ingrese calificaciones: "))
	cadenaFinal = ("%s%.2f\n"% (cadenaFinal, nota))
	salida = int(input("Ingrese (1) si desea salir del ciclo: "))
	if (salida== 1):
		bandera = False
print("Listado de Notas\n%s\n"% (cadenaFinal))		






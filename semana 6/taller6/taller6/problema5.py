##Se realiza una tabla de repeticion para presentar una tabla de notas y ver si esta aprobado y resprobado
contador = 1
cadenafinal = ""
while (contador <= 4):
	nombre = input("Ingrese el nombre del estudiante: ")
	promedio = float(input("Ingrese el promedio del ciclo: "))
	if (promedio >=7):
		estado ="Aprobado"
	else:
		estado ="Reprobado"
	cadenafinal = ("%s%s\t%.2f\t%s\t\n"%(cadenafinal,nombre,promedio,estado))
	contador = contador + 1
print ("%s\n"%(cadenafinal))		







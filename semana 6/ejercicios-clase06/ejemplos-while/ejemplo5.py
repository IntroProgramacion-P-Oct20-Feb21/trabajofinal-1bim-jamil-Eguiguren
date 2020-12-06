## Se raliza una condicion de repeticion para poder carlcular un promedio de notas
limite = 3
contador = 1
suma_total = 0
print("Ingrese las notas de los estudiantes de su materia")
while (contador <= limite):
	calificacion = float(input("Ingrese calificación número: %d\n"% (contador)))
	suma_total = suma_total + calificacion
	contador = contador + 1
promedio_final = suma_total / limite
print("El promedio  final es %.2f\n"% (promedio_final))





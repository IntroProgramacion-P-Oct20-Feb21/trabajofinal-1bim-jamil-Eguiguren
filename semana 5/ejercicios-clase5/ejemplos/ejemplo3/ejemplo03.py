##Se presenta 10 y con el mensaje de aprobado ya que cumplio todas las condiciones
promedio = 10
if (promedio >= 7.5):
	print("Estudiante aprobado con un promedio: %.2f\n"% (promedio))
else:
	if ((promedio >= 5) and (promedio <= 7.4)):
		print("Estudiante en suspenso con un promedio: %.2f\n"% (promedio))
	else: 
		print("Estudiante reprobado con un promedio: %.2f\n"% (promedio))
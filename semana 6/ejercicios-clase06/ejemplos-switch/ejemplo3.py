##Se pide que ungrese un dia de la semana para luego presentar en pantalla dependiendo de que dia sea
cadena = input("Ingrese el nombre del día de la semana: ")
if (cadena=="lunes"):
	print("%s"% (cadena))
else:
	if ((cadena=="Martes") or (cadena=="martes")):
		print("%s"% (cadena))
	else:
		if ((cadena=="Jueves") or (cadena=="jueves")):
			print("%s"% (cadena))
		else:
			print("ninguna de las anteriores")






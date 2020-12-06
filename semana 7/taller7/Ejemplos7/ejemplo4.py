##Se genera una condicion en la cual el usuario puede ingresar las variables que quiea, gracias a la bandera , para luego ser presentada
cadenaReporte = ""
sumaEdades = 0
sumaEstaturas = 0.0
contadorIteraciones = 0
bandera = True
cadenaReporte = ("%sListado de Jugadores\n"% (cadenaReporte))
while(bandera):
	nombreJugador =input("Ingrese el nombre del Jugador: ")
	posicionCampo =input("Ingrese la posición en el campo: ")
	edad =int(input("Ingrese la edad del Jugador: "))
	estatura =float(input("Ingrese la estatura del jugador: "))
	sumaEdades =sumaEdades + edad
	sumaEstaturas = sumaEstaturas + estatura
	contadorIteraciones =contadorIteraciones + 1
	cadenaReporte = ("%s%d.) %s -%s-, edad %d,estatura %.2f\n"%(\
		cadenaReporte,\
		contadorIteraciones,\
		nombreJugador,\
		posicionCampo,\
		edad,\
		estatura))
	salir =input("Desea salir del ciclo; digite si: ")
	if(salir==("si")):
		bandera = False
promedioEdad = sumaEdades/contadorIteraciones
promedioEstatura = sumaEstaturas/contadorIteraciones
cadenaReporte = ("%sPromedio de edades: %.2f\n"% (cadenaReporte, promedioEdad))
cadenaReporte = ("%sPromedio de estaturas: %.2f\n"% (cadenaReporte, promedioEstatura))
print("%s\n"% (cadenaReporte))















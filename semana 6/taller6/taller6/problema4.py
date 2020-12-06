##Se creo una cadena de repeticion para que el usuario ingrese una tabla de variables la cual se presentara despues 
contador = 1
cadenafinal = ""
while (contador <= 10):
	jugador = input("Ingresar el nombre del jugador: ")
	puntos = float(input("Ingresar la cantidad de puntos que anoto en la temporada: "))
	faltas = float(input("Ingresar la cantidad de faltas de la temporada: "))
	cadenafinal = ("%s%s\t%f\t%f\n"%(cadenafinal,jugador,puntos,faltas))
	contador = contador + 1
print("%s\n"% (cadenafinal))	





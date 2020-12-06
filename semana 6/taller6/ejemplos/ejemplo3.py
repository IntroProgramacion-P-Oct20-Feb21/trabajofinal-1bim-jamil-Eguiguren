##Se una cuestion para que el usuario decida si quiere tabla de suma o de multilicacion
cadenaFinal = ""
contador = 1
tipoOperacion = input("indique que tipo de tabla quiere realizar\n"\
	"suma\n"\
	"o\n"\
	"multiplicacion: \n")
numeroTabla = int(input("Ingrese el número de tabla: \n"))
limiteTabla = int(input("Ingrese el limite de tabla: \n"))
if (tipoOperacion == "suma"):
	cadenaFinal = ("Tabla de sumar del %s%s\n"% (cadenaFinal,numeroTabla))
	while(contador <= limiteTabla):
		operacion = numeroTabla + contador
		cadenaFinal = ("%s%d + %d = %d\n"% (cadenaFinal,numeroTabla,contador,operacion))
		contador = contador + 1
	else:
		if (tipoOperacion == "multiplicacion"):
			cadenaFinal = ("Tabla de multiplicar del %s%s\n"% (cadenaFinal,numeroTabla))
			while(contador <= limiteTabla):
				operacion = numeroTabla * contador
				cadenaFinal = ("%s%d + %d = %d\n"% (cadenaFinal,numeroTabla,contador,operacion))
				contador = contador + 1
			else:
				cadenaFinal = ("Error en tipo de operación%s\n"% (cadenaFinal))
print("%s\n"% (cadenaFinal))				
			
				


		

		








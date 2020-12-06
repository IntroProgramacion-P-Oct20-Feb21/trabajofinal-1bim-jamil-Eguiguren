##Se genera un codigo de repeticion que se va a repetir hasta determinado numero
limite_inferior = 10
limite_superior = 20
contador = 10
suma = 0
while ((contador >= limite_inferior) and (contador <= limite_superior)):
 	suma = suma + contador
 	print("Contador %d\n"% (contador))
 	contador = contador + 2
print("La suma final es %d\n"% (suma))	




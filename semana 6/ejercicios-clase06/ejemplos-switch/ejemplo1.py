##Se tiene dos variables donde el usuario decide si sumar o restar
valor1 = int(input("Ingrese el primer valor la operación: "))
valor2 = int(input("Ingrese el segundo valor la operación: "))
resultado = 0
op = int(input("Selecciones la operación que desea realizar\nIngrese 1 para sumar \nIngrese 2 para restar \n"))

if (op==1):
	resultado = valor1 + valor2
else:
	if (op==2):
		resultado = valor1 - valor2
	else:
		print("Operación incorrecta")


print("El resultado de la operación es : %d\n"% (resultado))













                 
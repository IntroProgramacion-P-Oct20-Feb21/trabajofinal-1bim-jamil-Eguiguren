##Se realiza una condicion donde el usuario decide entre sumar restar y multiplicar las variables
valor1 = int(input("Ingrese el primer valor la operación: "))
valor2 = int(input("Ingrese el segundo valor la operación: "))

resultado = 0
op = int(input("Selecciones la operación que desea realizar\nIngrese 1 para sumar \nIngrese 2 para restar \nIngrese 3 para multiplicar\n"))

if (op==1):
	resultado = valor1 + valor2
	tipo = "suma"
else:
	if (op==2):
		resultado = valor1 - valor2
		tipo = "resta"
	else:
		if (op==3):
			resultado = valor1 * valor2
			tipo = "multiplicación"
		else:
			print("Operación incorrecta")

print("El resultado de la operación %s es: %d\n"%(\
	tipo,\
	resultado))
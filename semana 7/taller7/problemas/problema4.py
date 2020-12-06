##Se presenta una tabla de fracciones la cual esta dividida por los pares y impares gracias a la condicion MOD
numerador = 1
denominador = 1
contador = 1
while (contador<=8):
	if((contador%2)==0):
		print("-%d/%d "% (numerador, denominador))
	else:
		print("+%d/%d "% (numerador, denominador))
	contador = contador + 1
	denominador = denominador + 2
print()	

		




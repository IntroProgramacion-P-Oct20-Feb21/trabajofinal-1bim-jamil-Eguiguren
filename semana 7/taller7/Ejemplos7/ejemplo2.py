##Se presenta una tabla con fracciones las cuales fueron divididas en pares y impares
numerador = 1
denominador = 1
contador = 1
while (contador<=5):
	if((contador%2)==0):
		print("-%d/%d"% (numerador, denominador))
	else:
		print("+%d/%d"% (numerador, denominador))
	contador = contador + 1	
	denominador = denominador + 2
print()	






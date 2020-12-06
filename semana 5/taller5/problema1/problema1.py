##Se genera una condisipn que nos ayuda a calcular una planilla de luz solo ingresando los datos
descuento = (0.10)
edad = int(input("Ingrese su edad "))
kilovatiohora = float(input("Ingrese la costo por kilovatio/hora "))
mes = float(input("Ingrese el numero de cunsumo de kilovatio al mes "))
multiplicacion =  kilovatiohora * mes
resta = multiplicacion * descuento
diezporciento = multiplicacion - resta
if (edad >65):
	print("el valor a cancelar de la planilla de luz con el 10%% es: %.2f"%(\
		diezporciento))
else:
	print("el valor a cancelar de la planilla de luz es: %.2f"%(multiplicacion))



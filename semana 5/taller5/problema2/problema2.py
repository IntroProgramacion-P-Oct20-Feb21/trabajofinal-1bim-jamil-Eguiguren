##Se realiza una condicion para poder calcular un decuenta dependiendo de cuantos articulos tenga
descuento =(0.15)
valor = float(input("Ingrese el valor del producto: "))
cantidad = float(input("Ingrese la cantidad deseada: "))
multiplicacion =  cantidad * valor
resta = multiplicacion * descuento
quince = multiplicacion - resta
if (cantidad >50):
	print("el valor a cancelar del articulo con el 15%% es: %.2f" %(quince))
else:
	print("el valor a cancelar del articulo es: %.2f" %(multiplicacion))
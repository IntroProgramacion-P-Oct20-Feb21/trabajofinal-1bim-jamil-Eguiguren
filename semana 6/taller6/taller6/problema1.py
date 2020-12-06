##Se realiza un codigo para poder carcular cuanto costara un descuento
netflix= 10
disney= 6
apple= 5
amazon= 4.5
resultadofinal = ""
nombre = input("Ingrese su nombre: ")
mensualidades = int(input("indique el numero de mensualidades (ingrese minimo 2):  "))
if (mensualidades >= 2 ):
	numero=int(input("indique que servicio de stream decea\n"\
		"Ingresar 1 para escoger netflix\n"\
		"Ingresar 2 para escoger disney\n"\
		"Ingresar 3 para escoger apple\n"\
		"Ingresar 4 para escoger amazon\n"))
	me_netflix = mensualidades * netflix
	me_disney = mensualidades * disney
	me_apple = mensualidades * apple
	me_amazon = mensualidades * amazon
	iva_netflix = me_netflix * 0.1
	iva_disney = me_disney * 0.12
	iva_apple = me_apple * 0.14
	iva_amazon = me_amazon * 0.16
	total_netflix = iva_netflix + me_netflix
	total_disney = iva_disney + me_disney
	total_apple = iva_apple + me_apple
	total_amazon = iva_amazon + me_amazon
else:
	resultadofinal = ("%sDatos erroneos\n",resultadofinal)
if (numero == 1):
	resultadofinal = ("Usuario:%s\nEmpresa: Netflix\nPrecio base: $%.2f\n"\
		"Impuesto: $%.2f\nTotal a cancelar: $%.2f\n"%(\
			nombre,\
			netflix,\
			iva_netflix,\
			total_netflix))
else:
	if (numero == 2):
		resultadofinal= ("Usuario:%s\nEmpresa: disney\nPrecio base: $%.2f\n"\
			"Impuesto: $%.2f\nTotal a cancelar: $%.2f\n"%(\
				nombre,\
				disney,\
				iva_disney,\
				total_disney))
	else:
		if (numero == 3):
			resultadofinal= ("Usuario:%s\nEmpresa: disney\nPrecio base: $%.2f\n"\
				"Impuesto: $%.2f\nTotal a cancelar: $%.2f\n"%(\
					nombre,\
					amazon,\
					iva_amazon,\
					total_amazon))
		else:
			if (numero == 4):
				resultadofinal= ("Usuario:%s\nEmpresa: disney\nPrecio base: $%.2f\n"\
					"Impuesto: $%.2f\nTotal a cancelar: $%.2f\n"%(\
						nombre,\
						amazon,\
						iva_amazon,\
						total_amazon))
print("%s\n"% (resultadofinal))					













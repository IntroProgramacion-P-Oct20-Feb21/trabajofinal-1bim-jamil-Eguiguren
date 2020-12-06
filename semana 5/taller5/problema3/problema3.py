##La salida se dara dependiendo de las condiciones ya que depende la ubicacion es como se realizara la operacion
descuento1 =(0.20)
descuento2 =(0.30)
descuento3 =(0.15)
descuento4 =(0.08)
marca = input("Ingrese la marca del carro: ")
origen = input("Ingrese el origen del carro: ")
precio = float(input("Ingrese el precio del carro: "))
resta1 = precio * descuento1
veinteporciento = precio - resta1
resta2 = precio * descuento2
treintaporciento = precio - resta2
resta3 = precio * descuento3
quinceporciento = precio - resta3
resta4 = precio * descuento4
ochoporciento = precio - resta4

if (origen==("Alemania")):
	print("Marca del carro: %s\nValor del impuesto: %.3f\nValor de precio de venta: %.3f\n"%(\
            marca,\
            resta1,\
            veinteporciento))
else:
	if (origen==("Japon")):
		print("Marca del carro: %s\nValor del impuesto: %.3f\nValor de precio de venta: %.3f\n"%(\
            marca,\
            resta2,\
            treintaporciento))
	else:
		if (origen==("Italia")):
			print("Marca del carro: %s\nValor del impuesto: %.3f\nValor de precio de venta: %.3f\n"%(\
             marca,\
             resta3,\
             quinceporciento))
		else:
			if (origen==("USA")):
				print("Marca del carro: %s\nValor del impuesto: %.3f\nValor de precio de venta: %.3f\n"%(\
                marca,\
                resta4,\
                ochoporciento))













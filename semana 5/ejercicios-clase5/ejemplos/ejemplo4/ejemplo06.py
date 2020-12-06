##Se pide que ingresen una variable en mayusculas solo la primera letra si esta bien va a imprmir correcto y si no incorrecto
ciudad = input("Ingrese la ciudad: ")
inicial = ciudad[0]
if (inicial==("L")):
	print("%s\n"% ("acceso correcto"))
else:
	print("%n\n"%("acceso incorrecto"))
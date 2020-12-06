##Se realiza una condicipmal para determinar que inicial tiene la palabra
nombre = input("Ingrese el nombre de una ciudad del Ecuador: ")
nombre = nombre.lower()
inicial = nombre[0]
if ((inicial=="a") or (inicial=="A")):
	print("Nombre con inicial %s de %s\n"% (inicial, nombre))
else:
	if ((inicial=="e") or (inicial=="E")):
		print("Nombre con inicial %s de %s\n"% (inicial, nombre))
	else:
		if ((inicial=="i") or (inicial=="I")):
			print("Nombre con inicial %s de %s\n"% (inicial, nombre))
		else:
			if ((inicial=="o") or (inicial=="O")):
				print("Nombre con inicial %s de %s\n"% (inicial, nombre))
			else:
				if ((inicial=="u") or (inicial=="U")):
					print("Nombre con inicial %s de %s\n"% (inicial, nombre))
				else:
					print("opción incorrecta; ninguna de las anteriores")









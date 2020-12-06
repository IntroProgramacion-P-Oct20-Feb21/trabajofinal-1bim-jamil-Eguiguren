##Se pide que ingrese una variable si esa variable es correcto, se presenta como si fuera incorrecta, si si no es la misma es correccta
ciudad = input("Ingrese la ciudad")
if(not ciudad==("Loja")):
	print("%s\n"% ("acceso correcto"))
else:
	print("%s\n"% ("acceso incorrecto"))

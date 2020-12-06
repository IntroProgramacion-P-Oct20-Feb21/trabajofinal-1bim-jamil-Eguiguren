##Solo se utilza una acomulador para tener que presentar solo un print
pais = "Ecuador"
ciudad = "Loja"
fechaIndependencia = "18 de noviembre"
cadenaAcumuladora = ""
cadenaAcumuladora = ("%s%s\n%s\n%s\n"%(\
	cadenaAcumuladora,\
	pais,\
	ciudad,\
	fechaIndependencia))
print("%s"% (cadenaAcumuladora))